from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
import datetime
from django.contrib.auth.models import User

# Create your models here.
options3 = [
    ('dedektiv', 'Dedektiv'),
    ('fantastik', 'Fantastik'),
    ('psixoloji', 'Psixoloji'),
    ('huquq', 'Hüquq'),
    ('roman', 'Roman'),
    ('dunya_edebiyyati', 'Dünya ədəbiyyatı'),
    ('felsefe', 'Fəlsəfə'),
]


class Kitablar(models.Model):
    Ad = models.CharField(max_length=70, verbose_name='Ad')
    Mezmun = RichTextField(default="", verbose_name='Məzmun')
    Yazar = models.CharField(max_length=25, default="", verbose_name='Yazar')
    Qiymet = models.CharField(max_length=8, default='', verbose_name='Qiymət')
    shekil = models.ImageField(verbose_name='Şəkil', default='')
    tarix = models.DateTimeField(
        auto_now_add=True, verbose_name="Əlavə edildiyi tarix")
    janr = models.CharField(max_length=20, choices=options3,
                            )
    options1 = (('Mövcud', 'mövcud'),
                ('Mövcud deyil', 'mövcud deyil'))

    options2 = (('Yeni', 'yeni'),
                ('İşlənmiş', 'işlənmiş'))

    options4 = (('Azərbaycan', 'Azərbaycan'),
                ('Türkçe', 'Türkçe'),
                ('Руский ', 'Руский '),
                ('English', 'English'))
    icare_ucun = models.CharField(
        max_length=20, choices=options1, verbose_name='Kirayə üçün mövcudluğu')
    veziyyet = models.CharField(
        max_length=20, choices=options2, verbose_name='Vəziyyəti', default='')

    dil = models.CharField(max_length=100, choices=options4,
                           verbose_name='Dil', default='')

    favourite = models.ManyToManyField(
        User, related_name='favourite', blank=True)

    def __str__(self):
        return self.Ad

    class Meta:
        verbose_name_plural = 'Kitablar'
        ordering = ['tarix']
