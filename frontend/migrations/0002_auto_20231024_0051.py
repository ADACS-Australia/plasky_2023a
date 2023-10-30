# Generated by Django 3.2 on 2023-10-24 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='h1',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='k1',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='l1',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='v1',
        ),
        migrations.AddField(
            model_name='subject',
            name='detectors',
            field=models.IntegerField(default=0),
        ),
    ]