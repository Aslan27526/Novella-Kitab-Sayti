# Generated by Django 2.2.1 on 2019-11-20 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0019_auto_20190909_0325'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kitablar',
            options={'ordering': ['tarix']},
        ),
    ]
