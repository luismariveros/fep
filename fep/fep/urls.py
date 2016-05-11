from django.conf.urls import patterns, include, url
from inscripciones import api

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'inscripciones.views.inicio', name='inicio'),
    url(r'^inscripcion/$', 'inscripciones.views.agregar_persona_view', name='vista_persona_agregar'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^contacto/', 'inscripciones.views.contacto_view', name='vista_contacto'),
    url(r'^departamentos/(?P<id_departamento>[0-9]+)/localidades/$', api.LocalidadList.as_view()),

)
