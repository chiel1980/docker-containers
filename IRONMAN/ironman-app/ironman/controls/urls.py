from django.conf.urls import url

from controls import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
