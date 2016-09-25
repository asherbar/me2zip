from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url('^admin/', admin.site.urls),
    url('^$', views.index, name='index')
]
