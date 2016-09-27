import os

from django.shortcuts import render

_GOOGLE_MAPS_API_KEY = os.environ['GOOGLE_MAPS_API_KEY']


class _Context(dict):
    REQUIRED_KEYS_DEFAULTS = {
        'latitude': None, 'longitude': None, 'gm_api_key': _GOOGLE_MAPS_API_KEY, 'search_id': None, 'resolved_zip': None
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
    context = _Context(latitude=latitude, longitude=longitude)
    return render(request, 'me2zip_main/home.html', context=context)
