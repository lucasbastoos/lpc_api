from tastypie.resources import ModelResource
from tastypie import fields, utils
from evento.models import *
from django.contrib.auth.models import User
from tastypie.authorization import Authorization

class TipoInscricaoResource(ModelResource):
    class Meta:
        resource_name = 'tipo'
        queryset = TipoInscricao.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        filtering = {
            "descricao": ('exact', 'startswith', 'endswith', 'contains',) # pra ser igual a palavra usa =    pra ser startswith usa __nome do metodo  e assim por diante
        }

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['password', 'is_active']

class PessoaFisicaResource(ModelResource):
    class Meta:
        resource_name = 'pf'
        queryset = PessoaFisica.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        filtering = {'cpf':('exact', 'startswith', 'endswith', 'contains')}


class PessoaResource(ModelResource):
    class Meta:
        resource_name = 'pessoa'
        queryset = Pessoa.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        filtering = {'nome':('exact', 'startswith', 'endswith', 'contains')}


class PessoaJuridicaResource(ModelResource):
    class Meta:
        resource_name = 'pj'
        queryset = PessoaJuridica.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        filtering = {'cnpj':('exact', 'startswith', 'endswith', 'contains')}


class EventoResource(ModelResource):
    realizador = fields.ToOneField(PessoaResource, 'realizador')
    class Meta:
        resource_name = 'evento'
        queryset = Evento.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        filtering = {'palavrasChave' : ('exact', 'startswith', 'contains')}

class EventoCientificoResource(ModelResource):
    class Meta:
        resource_name = 'eventoCientifico'
        queryset = EventoCientifico.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        filtering = {'issn' : ('exact', 'startswith', 'contains, endswith')}


class InscricaoResource(ModelResource):
    pessoa = fields.ToOneField(PessoaFisicaResource, 'pessoa') # ToOneField = de 1 pra 1 toManyField = de 1 pra muitos
    evento = fields.ToOneField(EventoResource, 'evento')
    tipo = fields.ToOneField(TipoInscricaoResource, 'tipoInscricao') #recurso que vai fazer o relacionamento e nome do campo no models
    class Meta:
        resource_name = 'inscricao'
        queryset = Inscricoes.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()

class ArtigoAutorResource(ModelResource):
    class Meta:
        resource_name = 'artigoAutor'
        queryset = ArtigoAutor.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        filtering = {'palavrasChave' : ('exact', 'startswith', 'contains')}

class ArtigoCientificoResource(ModelResource):
    class Meta:
        resource_name = 'artigo'
        queryset = ArtigoCientifico.objects.all()
        allowed_methods = ['get', 'post', 'delete', 'put']
        authorization = Authorization()
        filtering = {'titulo': ('exact', 'startswith', 'endswith, contains')}
