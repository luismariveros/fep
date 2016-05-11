from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from models import *
from . import resources

class PaisAdmin(ImportExportModelAdmin):
    list_display = ('id', 'nombre',)
    search_fields = ['nombre']
    resource_class = resources.PaisResource


class DepartamentoAdmin(ImportExportModelAdmin):
    list_display = ('id', 'nombre', 'pais',)
    search_fields = ['nombre']
    resource_class = resources.DepartamentoResource


class LocalidadAdmin(ImportExportModelAdmin):
    list_display = ('id', 'nombre', 'departamento',)
    search_fields = ['nombre']
    list_filter = ['departamento']
    resource_class = resources.LocalidadResource


class CiudadAdmin(ImportExportModelAdmin):
    list_display = ('id', 'nombre',)
    search_fields = ['nombre']
    resource_class = resources.CiudadResource


class OcupacionAdmin(ImportExportModelAdmin):
    list_display = ('id', 'nombre',)
    search_fields = ['nombre']
    resource_class = resources.OcupacionResource


class GrupoAdmin(ImportExportModelAdmin):
    list_display = ('id', 'nombre',)
    search_fields = ['nombre']
    resource_class = resources.GrupoResource


class TipoMovilidadAdmin(ImportExportModelAdmin):
    list_display = ('id', 'nombre',)
    search_fields = ['nombre']
    resource_class = resources.TipoMovilidadResource


class MovimientoAdmin(ImportExportModelAdmin):
    list_display = ('id', 'nombre',)
    search_fields = ['nombre']
    resource_class = resources.MovimientoResource


class InstitucionEducativaAdmin(ImportExportModelAdmin):
    list_display = ('id', 'nombre',)
    search_fields = ['nombre']
    resource_class = resources.InstitucionEducativaResource


class DiocesisAdmin(ImportExportModelAdmin):
    list_display = ('id', 'nombre',)
    search_fields = ['nombre']
    resource_class = resources.DiocesisResource


class DecanatoAdmin(ImportExportModelAdmin):
    list_display = ('id', 'nombre',)
    search_fields = ['nombre']
    resource_class = resources.DecanatoResource


class ParroquiaAdmin(ImportExportModelAdmin):
    list_display = ('id', 'nombre',)
    search_fields = ['nombre']
    resource_class = resources.ParroquiaResource


# Register your models here.
admin.site.register(Pais, PaisAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Localidad, LocalidadAdmin)
admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(Voluntario)
admin.site.register(Grupo, GrupoAdmin)
admin.site.register(Ocupacion, OcupacionAdmin)
admin.site.register(TipoMovilidad, TipoMovilidadAdmin)
admin.site.register(Movimiento, MovimientoAdmin)
admin.site.register(InstitucionEducativa, InstitucionEducativaAdmin)
admin.site.register(Diocesis, DiocesisAdmin)
admin.site.register(Decanato, DecanatoAdmin)
admin.site.register(Parroquia, ParroquiaAdmin)