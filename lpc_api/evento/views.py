from django.http import HttpResponse
from .models import Evento, EventoCientifico, Pessoa, PessoaFisica, PessoaJuridica, Autor, ArtigoCientifico, ArtigoAutor, Inscricoes, TipoInscricao

def index(request):
    html = """<h1>Opções</h1>
                <ul>
                    <li><a href='/eventos'>Eventos</a></li>
                    <li><a href='/eventoscientificos'>Eventos Científicos</a></li>
                    <li><a href='/pessoas'>Pessoas</a></li>
                    <ul>
                        <li><a href='/pessoasfisicas'>Pessoas Físicas</a></li>
                        <li><a href='/pessoasjuridicas'>Pessoas Jurídicas</a></li>
                    </ul>
                    <li><a href='/autores'>Autores</a></li>
                    <li><a href='/artigoscientificos'>Artigos Científicos </a></li>
                </ul>
            """
    return HttpResponse(html)

def listaEventos(request):
    html = "<h1>Lista de Eventos</h1>"
    listaEvento = Evento.objects.all()
    for evento in listaEvento:
        html += '<li><strong>{}</strong></li>'.format(evento.nome)
        html += '<ul><li>EventoPrincipal: {}</li>'.format(evento.eventoPrincipal)
        html += '<li>Cidade/UF: {}/{}</li>'.format(evento.cidade, evento.uf)
        html += '<li>Endereço: {}</li></ul>'.format(evento.endereco)
    return HttpResponse(html)

def eventoid(request, id):
    evt = Evento.objects.get(pk=id)
    return HttpResponse("<h2> Informações Evento #" + str(evt.id) + "</h2>" + "<strong>Nome:</strong> " + str(evt.nome)  + "<br>" + "<strong>Sigla:</strong> " + str(evt.sigla)  + "<br>" + "<strong>Endereço:</strong> " + str(evt.endereco) + "<br>" + "<strong>Realizador:</strong> " + str(evt.realizador.nome))

def listaEventoCientifico(request):
    html = "<h1>Lista de Eventos Científicos</h1>"
    listaEventoC = EventoCientifico.objects.all()
    for eventoC in listaEventoC:
        html += '<li><strong>{}</strong></li>'.format(eventoC.nome)
        html += '<ul><li>ISSN: {}</li>'.format(eventoC.issn)
        html += '<li>Cidade/UF: {}/{}</li>'.format(eventoC.cidade, eventoC.uf)
        html += '<li>Endereço: {}</li></ul>'.format(eventoC.endereco)
    return HttpResponse(html)

def eventoCientificoid(request, id):
    evtCientifico= EventoCientifico.objects.get(pk=id)
    return HttpResponse("<h2> Informações Evento Científico #" + str(evtCientifico.id) + "</h2>" + "<strong>Nome:</strong> " + str(evtCientifico.nome)  + "<br>" + "<strong>Sigla:</strong> " + str(evtCientifico.sigla)  + "<br>" + "<strong>ISSN:</strong> " + str(evtCientifico.issn) + "<br>" + "<strong>Realizador:</strong> " + str(evtCientifico.realizador.nome))

def listaPessoas(request):
    html = "<h1>Lista de Pessoas</h1>"
    listaPessoa = Pessoa.objects.all()
    for pessoa in listaPessoa:
        html += '<li><strong>{}</strong></li>'.format(pessoa.nome)
        html += '<ul><li>Email: {}</li></ul>'.format(pessoa.email)
    return HttpResponse(html)

def pessoaid(request, id):
    p = Pessoa.objects.get(pk=id)
    return HttpResponse("<h2> Informações Pessoa #" + str(p.id) + "</h2>" + "<strong>Nome:</strong> " + str(p.nome)  + "<br>" + "<strong>Email:</strong> " + str(p.email))
    
def listaPessoasFisicas(request):
    html = "<h1>Lista de Pessoas Físicas</h1>"
    listaPessoaFisica = PessoaFisica.objects.all()
    for pessoaF in listaPessoaFisica:
        html += '<li><strong>{}</strong></li>'.format(pessoaF.nome)
        html += '<ul><li>Email: {}</li>'.format(pessoaF.email)
        html += '<li>CPF: {}</li></ul>'.format(pessoaF.cpf)
    return HttpResponse(html)

def pessoaFisicaid(request, id):
    pFisica= PessoaFisica.objects.get(pk=id)
    return HttpResponse("<h2> Informações Pessoa Física #" + str(pFisica.id) + "</h2>" + "<strong>Nome:</strong> " + str(pFisica.nome)  + "<br>" + "<strong>Email:</strong> " + str(pFisica.email)  + "<br>" + "<strong>CPF:</strong> " + str(pFisica.cpf))

def listaPessoasJuridicas(request):
    html = "<h1>Lista de Pessoas Jurídicas</h1>"
    listaPessoaJuridica = PessoaJuridica.objects.all()
    for pessoaJ in listaPessoaJuridica:
        html += '<li><strong>{}</strong></li>'.format(pessoaJ.nome)
        html += '<ul><li>Email: {}</li>'.format(pessoaJ.email)
        html += '<li>CNPJ: {}</li></ul>'.format(pessoaJ.cnpj)
    return HttpResponse(html)

def pessoaJuridicaid(request, id):
    pJuridica= PessoaJuridica.objects.get(pk=id)
    return HttpResponse("<h2> Informações Pessoa Jurídica #" + str(pJuridica.id) + "</h2>" + "<strong>Nome:</strong> " + str(pJuridica.nome)  + "<br>" + "<strong>Email:</strong> " + str(pJuridica.email)  + "<br>" + "<strong>CNPJ:</strong> " + str(pJuridica.cnpj) + "<br>" + "<strong>Razão Social:</strong> " + str(pJuridica.razaoSocial))

def listaAutores(request):
    html = "<h1>Lista de Autores</h1>"
    listaAutor = Autor.objects.all()
    for autor in listaAutor:
        html += '<li><strong>{}</strong></li>'.format(autor.nome)
        html += '<ul><li>Email: {}</li>'.format(autor.email)
        html += '<li>Curriculo: {}</li></ul>'.format(autor.curriculo)
    return HttpResponse(html)

def autorid(request, id):
    html = " "
    autorCient= Autor.objects.get(pk=id)
    listaArtigos = ArtigoAutor.objects.filter(autor=id)
    for artigo in listaArtigos:
        html += '<li>{} </li>'.format(artigo.artigoCientifco.titulo)
    return HttpResponse("<h2> Informações Autor #" + str(autorCient.id) + "</h2>" + "<strong>Nome:</strong> " + str(autorCient.nome)  + "<br>" + "<strong>Email:</strong> " + str(autorCient.email)  + "<br>" + "<strong>Curriculo:</strong> " + str(autorCient.curriculo) + "<br>" + "<strong>Artigo(s):</strong> " + str(html))

def listaArtigosCientificos(request):
    html = "<h1>Lista de Artigos Científicos</h1>"
    listaArtigoCientifico = ArtigoCientifico.objects.all()
    for artigoC in listaArtigoCientifico:
        html += '<li><strong>{}</strong></li>'.format(artigoC.titulo)
        html += '<ul><li>Evento Científico Relacionado: {}</li></ul>'.format(artigoC.evento.nome)
    return HttpResponse(html)

def artigocientificoid(request, id):
    html = " "
    artigo= ArtigoCientifico.objects.get(pk=id)
    listaAutores= ArtigoAutor.objects.filter(artigoCientifco=id)
    for autorArtigo in listaAutores:
        html += '<li>{}</li>'.format(autorArtigo.autor.nome)

    return HttpResponse("<h2> Informações Artigo Científico #" + str(artigo.id) + "</h2>" + "<strong>Título:</strong> " + str(artigo.titulo)  + "<br>" + "<strong>Evento Científico Relacionado:</strong> " + str(artigo.evento.nome)  + "<br>" + "<strong>Autores:</strong> " + str(html))

def listainscricoes(request, id):
    html = " "
    eventoInsc= Evento.objects.get(pk=id)
    listainscritos= Inscricoes.objects.filter(evento=id)
    for inscrito in listainscritos:
        html += '<li><strong>Nome:</strong> {} </strong> <strong>E-mail:</strong> {} <strong>CPF:</strong> {}</li>'.format(inscrito.pessoa.nome, inscrito.pessoa.email, inscrito.pessoa.cpf)

    return HttpResponse("<h2> Lista de Inscritos do Evento #" + str(eventoInsc.nome) + "</h2>" + "<strong>Inscritos:</strong> " + str(html))
