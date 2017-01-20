from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^ninjas$', views.showAll),
    url(r'^ninjas/(?P<word>\w+)$', views.show)
]
