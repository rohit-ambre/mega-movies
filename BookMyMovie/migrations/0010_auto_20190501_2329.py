# Generated by Django 2.1.7 on 2019-05-01 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookMyMovie', '0009_auto_20190414_2336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='theatre',
        ),
    ]
