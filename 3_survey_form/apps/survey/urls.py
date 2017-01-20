from django.conf.urls import url
from . import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^result$', views.result),
    url(r'^reset$', views.reset)

]
