import logging
import os

from django.shortcuts import render
from zip_by_address.address import Address
from zip_by_address.address_by_coordinates.address_by_coordinates_resolver import AddressByCoordinatesResolver
from zip_by_address.address_by_coordinates.address_by_coordinates_resolver_factory import AddressByCoordinatesClsFactory
from zip_by_address.coordinates_by_address.coordinates_by_address_resolver import CoordinatesByAddressResolver
from zip_by_address.exceptions import NoSuchAddress
from zip_by_address.zip_by_address_resolver_factory import ZipResolverClsFactory

_GOOGLE_MAPS_API_KEY = os.environ['GOOGLE_MAPS_API_KEY']


class _Context(dict):
    REQUIRED_KEYS_DEFAULTS = {
        'latitude': None, 'longitude': None, 'gm_api_key': _GOOGLE_MAPS_API_KEY, 'search_id': None,
        'resolved_zip': None, 'resolved_address': None,
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for key, default in self.REQUIRED_KEYS_DEFAULTS.items():
            if key not in self:
                self[key] = default


def index(request):
    return render(request, 'me2zip_main/home.html', _Context())


def get_address_from_lat_long(request, latitude, longitude):
    try:
        country = _get_country_from_coords(latitude, longitude)
    except RuntimeError as e:
        return _get_invalid_lat_long_render(request, latitude, longitude, e)
    try:
        address_by_coords_localized_resolver_cls = AddressByCoordinatesClsFactory(country).create()
    except KeyError:
        return _get_unsupported_country_render(country, request)
    try:
        resolved_address = address_by_coords_localized_resolver_cls(latitude=latitude,
                                                                    longitude=longitude).resolve_address()
    except RuntimeError:
        resolved_address = None
    context = _Context(latitude=latitude, longitude=longitude, resolved_address=resolved_address)
    return render(request, 'me2zip_main/resolved_address.html', context=context)


def get_zip_from_address(request, latitude=None, longitude=None, country='', state='', city='',
                         street='', street_number=''):
    country = request.GET.get('country', country)
    state = request.GET.get('state', state)
    city = request.GET.get('city', city)
    street = request.GET.get('street', street)
    street_number = request.GET.get('street_number', street_number)
    resolved_address = Address(country, state, city, street, street_number)
    if latitude is None or longitude is None:
        latitude, longitude = _get_lat_long_from_address(resolved_address)
    try:
        country_by_coords = _get_country_from_coords(latitude, longitude)
    except RuntimeError as e:
        return _get_invalid_lat_long_render(request, latitude, longitude, e)
    try:
        zip_by_address_localized_resolver_cls = ZipResolverClsFactory(country_by_coords).create()
    except KeyError:
        return _get_unsupported_country_render(country, request)
    try:
        resolved_zip = zip_by_address_localized_resolver_cls(resolved_address).resolve_zip()
    except (ValueError, NoSuchAddress):
        resolved_zip = ''
    context = _Context(latitude=latitude, longitude=longitude, resolved_address=resolved_address,
                       resolved_zip=resolved_zip)
    return render(request, 'me2zip_main/resolved_zip.html', context=context)


def about(request):
    return render(request, 'me2zip_main/about.html',
                  context={'available_countries': ZipResolverClsFactory.get_supported_countries()})


def api(request):
    return render(request, 'me2zip_main/api.html')


def help_page(request):
    return render(request, 'me2zip_main/help.html')


def _get_country_from_coords(latitude, longitude):
    address_by_coords_standard_resolver = AddressByCoordinatesResolver(latitude=latitude, longitude=longitude)
    return address_by_coords_standard_resolver.resolve_address().country


def _get_unsupported_country_render(country, request):
    return render(request, 'me2zip_main/errors/country_not_supported.html', context=_Context(country=country))


def _get_lat_long_from_address(address):
    return CoordinatesByAddressResolver(address).resolve_coords()


def _get_invalid_lat_long_render(request, latitude, longitude, exception):
    logger = logging.getLogger('views')
    logger.error(str(exception))
    return render(request, 'me2zip_main/errors/invalid_lat_long.html', context=_Context(latitude=latitude,
                                                                                        longitude=longitude))
