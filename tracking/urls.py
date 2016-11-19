from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^search/', views.search, name='search'),
	url(r'^create/', views.create, name='create'),
	url(r'^data/', views.data, name='data'),
	url(r'^detail/(?P<asset_catalog_id>[0-9]+)/$', views.detail, name='detail'),

]