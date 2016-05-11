# coding=utf8
# -*- coding: utf8 -*-
from django.db import models


class MiForm(models.Model):
    error_css_class = 'list-group-item-danger'

    def __init__(self, *args, **kwargs):
        super(MiForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class Grupo(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    responsable = models.ForeignKey("Voluntario", related_name="responsable", blank=True, null=True)
    grupo_padre = models.ForeignKey("self", blank=True, null=True)
    cantidad = models.PositiveIntegerField(blank=True, null=True, default=None)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Grupos"


class Pais(models.Model):
    id = models.CharField(max_length=2, primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre")

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Países"


class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais)

    class Meta:
        verbose_name = "departamento"
        verbose_name_plural = "departamentos"
        ordering = ['nombre']

    def __unicode__(self):
        return self.nombre


class Localidad(models.Model):
    nombre = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento)

    class Meta:
        verbose_name = "localidad"
        verbose_name_plural = "localidades"
        ordering = ['nombre']

    def __unicode__(self):
        return self.nombre


class Ciudad(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    departamento = models.ForeignKey(Departamento, default=None, blank=True, null=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Ciudades"


class Ocupacion(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Ocupaciones"


class TipoMovilidad(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Tipos de Movilidad"


class Movimiento(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Movimientos"


class InstitucionEducativa(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Instituciones Educativas"


class Diocesis(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Diócesis"


class Decanato(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    diocesis = models.ForeignKey(Diocesis)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Decanatos"


class Parroquia(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    diocesis = models.ForeignKey(Diocesis, blank=True, null=True, default=None)
    decanato = models.ForeignKey(Decanato, blank=True, null=True, default=None)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Parroquias"


class Voluntario(models.Model):
    MASCULINO = 'M'
    FEMENINO = 'F'
    SEXO_OPCIONES = (
        (MASCULINO, 'Masculino'),
        (FEMENINO, 'Femenino')
    )
    TIPO_DOCUMENTO = (
        ('CI', 'Cédula de Identidad'),
        ('PA', 'Pasaporte')
    )
    VOIP_TIPO = (
        ('SKYPE', 'Skype'),
        ('HANGOUT', 'Hangout'),
        ('OTRO', 'Otro'),
        ('NOUSO', 'No uso')
    )

    nombre = models.CharField(max_length=100, verbose_name="Nombres (*)")
    apellido_paterno = models.CharField(max_length=100, verbose_name="Primer Apellido (*)")
    apellido_materno = models.CharField(max_length=100, verbose_name="Segundo Apellido", blank=True, null=True)
    sexo = models.CharField(max_length=50, choices=SEXO_OPCIONES, verbose_name="Sexo (*)")
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento (*)")
    nacionalidad = models.ForeignKey(Pais, related_name="nacionalidad")
    telefono = models.CharField(max_length=40, verbose_name="Teléfono (*)")
    email = models.EmailField(verbose_name="Email (*)")
    documento_tipo = models.CharField(max_length=50, choices=TIPO_DOCUMENTO, verbose_name="Tipo de Documento (*)")
    documento_numero = models.CharField(max_length=100, verbose_name="Número de Documento (*)")
    documento_pais_emisor = models.ForeignKey(Pais, related_name="pais_emisor",
                                              verbose_name="País Emisor del Documento (*)")
    documento_vencimiento = models.DateField(verbose_name="Fecha de Vencimiento del Documento (*)")
    # voip_tipo = models.CharField(max_length=50, choices=VOIP_TIPO, verbose_name="VOIP (*)")
    # voip_usuario = models.CharField(max_length=100, verbose_name="Nombre de usuario VOIP", blank=True, null=True)
    pais_residencia = models.ForeignKey(Pais, related_name="pais_residencia", verbose_name=" País de Residencia (*)")
    departamento_residencia = models.ForeignKey(Departamento, related_name="departamento_residencia",
                                                blank=True, null=True, verbose_name=" Departamento de Residencia (*)")
    localidad_residencia = models.ForeignKey(Localidad, related_name="localidad_residencia", blank=True, null=True,
                                             verbose_name=" Localidad de Residencia (*)")
    ciudad_residencia = models.ForeignKey(Ciudad, related_name="ciudad_residencia", blank=True, null=True,
                                          verbose_name=" Ciudad de Residencia (*)")
    direccion_residencia = models.CharField(max_length=300, verbose_name="Dirección en País de Residencia (*)")
    direccion_paraguay = models.CharField(max_length=300, verbose_name="Dirección en Paraguay", blank=True, null=True)
    # grupo = models.ForeignKey(Grupo, blank=True, null=True)
    ocupacion = models.ForeignKey(Ocupacion, verbose_name="Ocupación (*)")
    ocupacion_otros = models.CharField(max_length=100, verbose_name="Otra ocupación", blank=True, null=True)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)
    direccion_ip = models.IPAddressField(null=True)
    tiene_alguna_discapacidad = models.BooleanField(default=False,
                                                    verbose_name="¿Posee usted algún tipo de discapacidad?")
    necesita_alojamiento = models.BooleanField(default=False,
                                               verbose_name="¿Necesita alojamiento?")
    tipo_movilidad = models.ForeignKey(TipoMovilidad, blank=True, null=True, default=None,
                                       verbose_name="Si posee registro de conducir, que tipo de vehículo maneja.")
    movimiento = models.ForeignKey(Movimiento, blank=True, null=True, default=None, verbose_name="Movimiento")
    institucion_educativa = models.ForeignKey(InstitucionEducativa, blank=True, null=True, default=None,
                                              verbose_name="Institución Educativa")
    diocesis = models.ForeignKey(Diocesis, blank=True, null=True, default=None, verbose_name="Diócesis")
    decanato = models.ForeignKey(Decanato, blank=True, null=True, default=None, verbose_name="Decanato")
    parroquia = models.ForeignKey(Parroquia, blank=True, null=True, default=None, verbose_name="Parroquia", )


    def __unicode__(self):
        return self.nombre + self.apellido_paterno

    class Meta:
        verbose_name_plural = "Voluntarios"


class Contacto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre (*)")
    email = models.EmailField(verbose_name="Email (*)")
    asunto = models.CharField(max_length=100, verbose_name="Asunto", blank=True, null=True)
    mensaje = models.TextField(verbose_name="Mensaje (*)")

    def __unicode__(self):
        return "%s - %s" % (self.nombre + self.email)