# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=100)),
                ('texto', models.TextField()),
                ('published_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Depoimento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('published_date', models.DateTimeField(auto_now=True)),
                ('imagem', cloudinary.models.CloudinaryField(max_length=255, verbose_name='imagem')),
                ('autor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Destaque',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.CharField(max_length=300)),
                ('published_date', models.DateTimeField(auto_now=True)),
                ('imagem', cloudinary.models.CloudinaryField(max_length=255, verbose_name='imagem')),
                ('autor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('published_date', models.DateTimeField(auto_now=True)),
                ('imagem', cloudinary.models.CloudinaryField(max_length=255, verbose_name='imagem')),
            ],
        ),
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('localizacao', models.TextField()),
                ('tamanho', models.CharField(max_length=200)),
                ('published_date', models.DateTimeField(auto_now=True)),
                ('autor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='imagem',
            name='album',
            field=models.ForeignKey(to='myapp.Imovel', related_name='imagens'),
        ),
        migrations.AddField(
            model_name='contato',
            name='imovel',
            field=models.ForeignKey(to='myapp.Imovel', related_name='contatos'),
        ),
    ]
