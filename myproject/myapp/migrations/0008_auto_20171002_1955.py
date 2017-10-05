# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0007_document_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Depoimento',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('imagem', cloudinary.models.CloudinaryField(max_length=255, verbose_name='imagem')),
                ('autor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Destaque',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.CharField(max_length=300)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('imagem', cloudinary.models.CloudinaryField(max_length=255, verbose_name='imagem')),
                ('autor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, blank=True)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('imagem', cloudinary.models.CloudinaryField(max_length=255, verbose_name='imagem')),
            ],
        ),
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('localizacao', models.TextField()),
                ('tamanho', models.CharField(max_length=200)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('autor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='imagem',
            name='album',
            field=models.ForeignKey(related_name='imagens', to='myapp.Imovel'),
        ),
    ]
