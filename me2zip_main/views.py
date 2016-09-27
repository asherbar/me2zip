import os

from django.shortcuts import render


_GOOGLE_MAPS_API_KEY = os.environ['GOOGLE_MAPS_API_KEY']


def index(request):
    context = {
        'latitude': 0, 'longitude': 0, 'gm_api_key': _GOOGLE_MAPS_API_KEY
    }
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        context['search_id'] = search_id
    else:
        context['search_id'] = ''
    return render(request, 'me2zip_main/home.html', context=context)


def get_zip_from_lat_long(request, latitude, longitude):
    context = {
        'latitude': latitude, 'longitude': longitude, 'search_id': '', 'gm_api_key': _GOOGLE_MAPS_API_KEY
    }
    return render(request, 'me2zip_main/home.html', context=context)
