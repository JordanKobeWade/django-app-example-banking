# Generated by Django 2.2.6 on 2019-10-22 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20191021_2142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificatedeposit',
            name='status',
        ),
        migrations.RemoveField(
            model_name='certificatedepositira',
            name='status',
        ),
        migrations.RemoveField(
            model_name='checking',
            name='status',
        ),
        migrations.RemoveField(
            model_name='moneymarket',
            name='status',
        ),
        migrations.RemoveField(
            model_name='savings',
            name='status',
        ),
    ]
