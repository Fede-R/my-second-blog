from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^preferences/$', views.preferencePage, name='preferencePage'),
    url(r'^new/$', views.nuevoEnfermedadPage, name='nuevoEnfermedadPage'),
    url(r'^about/$', views.aboutUsPage, name='aboutUsPage'),
    url(r'^api/mireviews$', views.processMireviews, name='processMireviews'),
    url(r'^api/reviews$', views.processReviews, name='processReviews'),
    url(r'^api/dishes$', views.crearEnfermedad, name='crearEnfermedad'),
    url(r'^api/preferences$', views.newPreference, name='newPreference'),
    url(r'^api/modifications$', views.modify, name='modify'),
    url(r'^reporte/$', views.reportePage, name='reportePage'),
    url(r'^reportemaiz/$', views.reportemaizPage, name='reportemaizPage'),
]
