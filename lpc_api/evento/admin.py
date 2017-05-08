from django.contrib import admin
from evento.models import Evento, EventoCientifico, Pessoa, PessoaFisica, PessoaJuridica, Autor, ArtigoCientifico, Inscricoes, TipoInscricao, ArtigoAutor


admin.site.register(Evento)
admin.site.register(EventoCientifico)
admin.site.register(Pessoa)
admin.site.register(PessoaFisica)
admin.site.register(PessoaJuridica)
admin.site.register(Autor)
admin.site.register(ArtigoCientifico)
admin.site.register(Inscricoes)
admin.site.register(TipoInscricao)
admin.site.register(ArtigoAutor)
