# Generated by Django 2.2.6 on 2019-10-21 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20191021_0414'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='one_description',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='two_description',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
    ]
