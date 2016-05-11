# -*- encoding: utf-8 -*-
from django import forms
from models import *
from captcha.fields import CaptchaField

forms.DateInput.input_type = "text"


class VoluntarioForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Voluntario
        exclude = ['direccion_ip']

        widgets = {
            'fecha_nacimiento': forms.TextInput(attrs={'placeholder': 'Formato MM/DD/YYYY'}),
            'documento_vencimiento': forms.TextInput(attrs={'placeholder': 'Formato MM/DD/YYYY'}),
            'fecha_inscripcion': forms.TextInput(attrs={'placeholder': 'Formato MM/DD/YYYY'})
        }


class ContactoForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Contacto