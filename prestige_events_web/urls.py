from django.urls import path

from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
app_name = 'prestige_events_web'

urlpatterns = [
    path('', views.home, name='home'),
]

urlpatterns += staticfiles_urlpatterns()