from django.conf.urls import url
from django.contrib import admin

from . import views

_FLOAT_REGEX = '\d+\.\d+'

_ADDRESS_COMPONENT_REGEX = '[\w \-,]*'

urlpatterns = [
    url('^admin/', admin.site.urls),
    url('^$', views.index, name='index'),
    url('^lat=(?P<latitude>{0})&long=(?P<longitude>{0})$'.format(_FLOAT_REGEX), views.get_address_from_lat_long,
        name='address_from_lat_long'),
    url('^autolocate=(?P<autolocate_success>true|false)(&country=(?P<country>{0})&state=(?P<state>{0})'
        '&city=(?P<city>{0})&street=(?P<street>{0})&street_number=(?P<street_number>{0}))?$'.format(
        _ADDRESS_COMPONENT_REGEX), views.get_zip_from_address, name='zip_from_address'
    ),
]
