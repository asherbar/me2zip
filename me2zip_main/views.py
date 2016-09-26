from django.shortcuts import render


def index(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        context = {
            'search_id': search_id, 'latitude': 0, 'longitude': 0
        }
    else:
        context = {
            'search_id': '', 'latitude': 0, 'longitude': 0
        }
    return render(request, 'me2zip_main/home.html', context=context)


def get_zip_from_lat_long(request, latitude, longitude):
    context = {
        'latitude': latitude, 'longitude': longitude, 'search_id': '',
    }
    return render(request, 'me2zip_main/home.html', context=context)
