# Generated by Django 2.1.7 on 2019-09-08 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0016_auto_20190908_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitablar',
            name='dil',
            field=models.CharField(choices=[('Azərbaycan', 'Azərbaycan'), ('Türkçe', 'Türkçe'), (
                'Руский ', 'Руский '), ('English', 'English')], default='', max_length=100, verbose_name='Dil'),
        ),
    ]
