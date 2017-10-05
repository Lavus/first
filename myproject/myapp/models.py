# -*- coding: utf-8 -*-
from django.db.models import Model, ForeignKey, CharField, DateTimeField, TextField
from django.db.models.signals import post_delete, pre_save
from cloudinary.models import CloudinaryField
from django.utils.timezone import now
from django.dispatch import receiver
from cloudinary import uploader

class Imovel(Model):
    autor = ForeignKey('auth.User')
    titulo = CharField(max_length=200)
    descricao = TextField()
    localizacao = TextField()
    tamanho = CharField(max_length=200)
    published_date = DateTimeField()

    def publish(self):
        self.published_date = now()
        self.save()

    def __str__(self):
        return self.titulo

class Imagem(Model):
    album = ForeignKey('Imovel', related_name='imagens')
    titulo = CharField(max_length=100)
    published_date = DateTimeField()
    imagem = CloudinaryField('imagem')

    def __unicode__(self):
        try:
            public_id = self.imagem.public_id
        except AttributeError:
            public_id = ''
        return "Imagem <%s:%s>" % (self.titulo, public_id)

    def publish(self):
        self.published_date = now()
        self.save()

    def __str__(self):
        return self.titulo

@receiver(post_delete, sender=Imagem)
def auto_delete_imagem_of_Imagem_on_delete(sender, instance, **kwargs):
    if instance.imagem.public_id:
        uploader.destroy(instance.imagem.public_id,invalidate=True)

@receiver(pre_save, sender=Imagem)
def auto_delete_imagem_of_Imagem_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_file = Imagem.objects.get(pk=instance.pk).imagem.public_id
    except Imagem.DoesNotExist:
        return False
    new = True
    try:
        new_file = instance.imagem.public_id
    except:
        new = False
    if new == False:
        uploader.destroy(old_file,invalidate=True)

class Destaque(Model):
    autor = ForeignKey('auth.User')
    titulo = CharField(max_length=200)
    descricao = CharField(max_length=300)
    published_date = DateTimeField()
    imagem = CloudinaryField('imagem')

    def __unicode__(self):
        try:
            public_id = self.imagem.public_id
        except AttributeError:
            public_id = ''
        return "Imagem <%s:%s>" % (self.titulo, public_id)

    def publish(self):
        self.published_date = now()
        self.save()

    def __str__(self):
        return self.titulo

@receiver(post_delete, sender=Destaque)
def auto_delete_imagem_of_Destaque_on_delete(sender, instance, **kwargs):
    if instance.imagem.public_id:
        uploader.destroy(instance.imagem.public_id,invalidate=True)

@receiver(pre_save, sender=Destaque)
def auto_delete_imagem_of_Destaque_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_file = Destaque.objects.get(pk=instance.pk).imagem.public_id
    except Destaque.DoesNotExist:
        return False
    new = True
    try:
        new_file = instance.imagem.public_id
    except:
        new = False
    if new == False:
        uploader.destroy(old_file,invalidate=True)

class Depoimento(Model):
    autor = ForeignKey('auth.user')
    titulo = CharField(max_length=200)
    descricao = TextField()
    published_date = DateTimeField()
    imagem = CloudinaryField('imagem')

    def __unicode__(self):
        try:
            public_id = self.imagem.public_id
        except AttributeError:
            public_id = ''
        return "Imagem <%s:%s>" % (self.titulo, public_id)

    def publish(self):
        self.published_date = now()
        self.save()

    def __str__(self):
        return self.titulo

@receiver(post_delete, sender=Depoimento)
def auto_delete_imagem_of_Depoimento_on_delete(sender, instance, **kwargs):
    if instance.imagem.public_id:
        uploader.destroy(instance.imagem.public_id,invalidate=True)

@receiver(pre_save, sender=Depoimento)
def auto_delete_imagem_of_Depoimento_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_file = Depoimento.objects.get(pk=instance.pk).imagem.public_id
    except Depoimento.DoesNotExist:
        return False
    new = True
    try:
        new_file = instance.imagem.public_id
    except:
        new = False
    if new == False:
        uploader.destroy(old_file,invalidate=True)
