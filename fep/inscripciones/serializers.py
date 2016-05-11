# coding=utf8
# -*- coding: utf8 -*-

from rest_framework import serializers
from . import models


class LocalidadSerializer(serializers.ModelSerializer):
    """
    Serializador para modelo Localidad
    """
    class Meta:
        model = models.Localidad
        fields = ('id', 'nombre')
