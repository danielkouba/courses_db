from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^newcourse$', views.newcourse),
	url(r'^delete/(?P<courseID>\d+)$', views.delete),
	url(r'^processdelete/(?P<courseID>\d+)$', views.processdelete)

]
