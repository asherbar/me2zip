from django.conf.urls import url
from django.contrib import admin

from . import views

_FLOAT_REGEX = '\d+\.\d+'

_ADDRESS_COMPONENT_REGEX = '[\w \-,]*'

_MAP_COORDS_REGEX = 'mapcoords=(?P<latitude>{0}),(?P<longitude>{0})'.format(_FLOAT_REGEX)

urlpatterns = [
    url('^admin/', admin.site.urls),
    url('^$', views.index, name='index'),
    url(('^{}$'.format(_MAP_COORDS_REGEX)), views.get_address_from_lat_long,
        name='get_zip_from_lat_long'),
    url('^manual_address_input$', views.manual_address_input, name='manual_address_input'),
    url('^country=(?P<country>{0})&state=(?P<state>{0})&city=(?P<city>{0})&street=(?P<street>{0})'
        '&street_number=(?P<street_number>{0})'
        '(&{1})?$'.format(_ADDRESS_COMPONENT_REGEX, _MAP_COORDS_REGEX),
        views.get_zip_from_address, name='zip_from_address'),
]
