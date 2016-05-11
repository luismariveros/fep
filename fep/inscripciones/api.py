# coding=utf8
# -*- coding: utf8 -*-

from rest_framework import generics
from rest_framework.permissions import AllowAny
from . import models
from . import serializers


class LocalidadList(generics.ListAPIView):
    # queryset = models.Localidad.objects.all()
    serializer_class = serializers.LocalidadSerializer
    permission_classes = (AllowAny, )

    def get_queryset(self):

        id_departamento = self.kwargs['id_departamento']

        empleos_query = models.Localidad.objects\
            .filter(departamento__id=id_departamento)\
            .order_by('nombre')

        return empleos_query
