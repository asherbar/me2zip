from django.shortcuts import render


def index(request):
    return render(request, 'me2zip_main/home.html')
