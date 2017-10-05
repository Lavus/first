# -*- coding: utf-8 -*-
from django.forms import ModelForm
from myproject.myapp.models import Imagem, Imovel, Destaque, Depoimento

class ImagemForm(ModelForm):
    class Meta:
        model = Imagem
        fields = '__all__'

class ImovelForm(ModelForm):
    class Meta:
        model = Imovel
        fields = '__all__'

class DestaqueForm(ModelForm):
    class Meta:
        model = Destaque
        fields = '__all__'

class DepoimentoForm(ModelForm):
    class Meta:
        model = Depoimento
        fields = '__all__'
