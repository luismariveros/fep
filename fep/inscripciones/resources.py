from import_export import resources
from . import models


class PaisResource(resources.ModelResource):
    class Meta:
        model = models.Pais
        fields = ('id', 'nombre',)


class DepartamentoResource(resources.ModelResource):
    class Meta:
        model = models.Departamento
        fields = ('id', 'nombre', 'pais',)


class LocalidadResource(resources.ModelResource):
    class Meta:
        model = models.Localidad
        fields = ('id', 'nombre', 'departamento',)


class CiudadResource(resources.ModelResource):
    class Meta:
        model = models.Ciudad
        fields = ('id', 'nombre',)


class OcupacionResource(resources.ModelResource):
    class Meta:
        model = models.Ocupacion
        fields = ('id', 'nombre',)


class GrupoResource(resources.ModelResource):
    class Meta:
        model = models.Grupo
        fields = ('id', 'nombre',)


class TipoMovilidadResource(resources.ModelResource):
    class Meta:
        model = models.TipoMovilidad
        fields = ('id', 'nombre',)


class MovimientoResource(resources.ModelResource):
    class Meta:
        model = models.Movimiento
        fields = ('id', 'nombre',)


class InstitucionEducativaResource(resources.ModelResource):
    class Meta:
        model = models.InstitucionEducativa
        fields = ('id', 'nombre',)


class DiocesisResource(resources.ModelResource):
    class Meta:
        model = models.Diocesis
        fields = ('id', 'nombre',)


class DecanatoResource(resources.ModelResource):
    class Meta:
        model = models.Decanato
        fields = ('id', 'nombre', 'diocesis',)


class ParroquiaResource(resources.ModelResource):
    class Meta:
        model = models.Parroquia
        fields = ('id', 'nombre', 'diocesis', 'decanato',)