from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add$', views.add, name='create'),
    url(r'^show/(?P<id>\d+)$', views.show, name='show'),
    url(r'^destroy/(?P<id>\d+)$', views.destroy, name='destroy'),
    url(r'^users_courses', views.users_courses, name='users_courses'),
    url(r'^add_student', views.add_student, name='add_student')
]
