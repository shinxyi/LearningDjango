from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'^show/(?P<id>\d+)$', views.show),
    url(r'^destroy/(?P<id>\d+)$', views.destroy),

]
