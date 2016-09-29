from django.conf.urls import url
from django.contrib import admin

from . import views

_FLOAT_REGEX = '\d+\.\d+'
urlpatterns = [
    url('^admin/', admin.site.urls),
    url('^$', views.index, name='index'),
    url('^lat=(?P<latitude>{0})&long=(?P<longitude>{0})$'.format(_FLOAT_REGEX), views.get_zip_from_lat_long)
]
