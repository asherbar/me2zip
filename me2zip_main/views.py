import os

from django.shortcuts import render
from zip_by_address.address_by_coordinates.address_by_coordinates_localizations.israel.\
    address_by_coordinates_resolver_israel import AddressByCoordinatesResolverIsrael
from zip_by_address.zip_by_address_localizations.israel.zip_by_address_israel import ZipByAddressIsrael

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
    context = _Context()
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        context['search_id'] = search_id
    return render(request, 'me2zip_main/home.html', context=context)


def get_zip_from_lat_long(request, latitude, longitude):
    resolved_address = AddressByCoordinatesResolverIsrael(latitude=latitude, longitude=longitude).resolve_address()
    resolved_zip = ZipByAddressIsrael(resolved_address).resolve_zip()
    context = _Context(latitude=latitude, longitude=longitude, resolved_zip=resolved_zip,
                       resolved_address=resolved_address)
    return render(request, 'me2zip_main/home.html', context=context)
