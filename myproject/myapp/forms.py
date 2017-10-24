# -*- coding: utf-8 -*-
from django.forms import ModelForm, HiddenInput
from myproject.myapp.models import Imagem, Imovel, Destaque, Depoimento, Contato


class ImovelForm(ModelForm):
    class Meta:
        model = Imovel
        fields = '__all__'

class ImagemForm(ModelForm):
    class Meta:
        model = Imagem
        fields = '__all__'

class ContatoForm(ModelForm):
    class Meta:
        model = Contato
        fields = '__all__'
        widgets = {'imovel': HiddenInput()}

class DestaqueForm(ModelForm):
    class Meta:
        model = Destaque
        fields = '__all__'

class DepoimentoForm(ModelForm):
    class Meta:
        model = Depoimento
        fields = '__all__'
