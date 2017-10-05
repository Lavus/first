# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.timezone import now
from myproject.myapp.models import Imovel, Destaque, Depoimento

def list(request):
    imoveis = Imovel.objects.all().order_by('published_date')
    destaques = Destaque.objects.all()
    depoimento = Depoimento.objects.all()
    pagin4 = range(4,(int(depoimento.count()/4)*4)+1,4)
    pagination4 = range(4,(int(imoveis.count()/4)*4)+1,4)
    pagination8 = range(8,(int(imoveis.count()/8)*8)+1,8)
    new_imoveis = []
    new_depoimento = []
    if len(imoveis) > 0:
        new_imoveis = [[[]]]
        i = 0
        x = 0
        for count, imovel in enumerate(imoveis):
            if count+1 in pagination8:
                new_imoveis[i][x].append({'imagem':imovel.imagens, 'titulo':imovel.titulo, 'descricao':imovel.descricao, 'localizacao':imovel.localizacao, 'tamanho':imovel.tamanho, 'published_date':imovel.published_date, 'id':imovel.id})
                if count+1 != len(imoveis):
                    new_imoveis.append([[]])
                i += 1
                x = 0
            elif count+1 in pagination4:
                new_imoveis[i][x].append({'imagem':imovel.imagens, 'titulo':imovel.titulo, 'descricao':imovel.descricao, 'localizacao':imovel.localizacao, 'tamanho':imovel.tamanho, 'published_date':imovel.published_date, 'id':imovel.id})
                new_imoveis[i].append([])
                x = 1
            else:
                new_imoveis[i][x].append({'imagem':imovel.imagens, 'titulo':imovel.titulo, 'descricao':imovel.descricao, 'localizacao':imovel.localizacao, 'tamanho':imovel.tamanho, 'published_date':imovel.published_date, 'id':imovel.id})   
    if len(depoimento) > 0:
        new_depoimento = [[]]
        i = 0
        for count, depoi in enumerate(depoimento):
            if count+1 in pagin4:
                new_depoimento[i].append({'imagem':depoi.imagem, 'titulo':depoi.titulo, 'descricao':depoi.descricao, 'published_date':depoi.published_date, 'id':depoi.id})
                if count+1 != len(depoimento):
                    new_depoimento.append([])
                i += 1
            else:
                new_depoimento[i].append({'imagem':depoi.imagem, 'titulo':depoi.titulo, 'descricao':depoi.descricao, 'published_date':depoi.published_date, 'id':depoi.id})

    context = {'destaques':destaques, 'new_depoimento':new_depoimento, 'pagination4':pagination4, 'pagination8':pagination8, 'new_imoveis':new_imoveis}
    return render_to_response(
        'index.html',
        context,
        context_instance=RequestContext(request)
    )

def undefined(request):
    return redirect(list)

#~ definir se slide com apenas uma imagem, colocar bruto como no depoimento
#~ colocar se não existe imagem, carregar sem imagem, o padrão que ele passou
#~ descricao colocar tres pontinhos caso passe de duzentos caracteres

