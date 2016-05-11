# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response, HttpResponseRedirect, RequestContext, Http404
from django.utils.translation import activate
from forms import *
from models import *
from django.template import Context, loader
from django.template.loader import get_template


from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.core.urlresolvers import reverse
activate('es')


def envio_mail(inscripto):
    htmly = get_template('emails/inscripcion.html')
    origen = 'Francisco en Paraguay <noreply@franciscoenparaguay.org>'
    asunto = '[FranciscoEnParaguay] Registro de Servidor'

    d = Context({'inscripto': inscripto})
    html_content = htmly.render(d)
    msg = EmailMultiAlternatives(asunto, html_content, origen, [inscripto.email])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


def inicio(request):
    return render_to_response('index.html', {}, context_instance=RequestContext(request))


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def cerrar_sesion(request):
    logout(request)
    return HttpResponseRedirect('/login')


def agregar_persona_view(request):

    if request.method == 'POST':
        formulario = VoluntarioForm(request.POST)
        if formulario.is_valid():
            persona = formulario.save(commit=False)
            persona.direccion_ip = get_client_ip(request)
            persona.save()
            envio_mail(persona)
            messages.success(request, 'Registro Exitoso. Se ha enviado un correo electrónico')
            return HttpResponseRedirect(reverse('vista_persona_agregar'))
    else:
        formulario = VoluntarioForm()

    return render_to_response(
        'form-persona.html',
        {'formulario': formulario},
        context_instance=RequestContext(request)
    )


def contacto_view(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Envio de Mensaje Exitoso.')
            return HttpResponseRedirect(reverse('vista_contacto'))
    else:
        form = ContactoForm()
    return render_to_response(
        'form-contacto.html',
        {'form': form},
        context_instance=RequestContext(request)
    )