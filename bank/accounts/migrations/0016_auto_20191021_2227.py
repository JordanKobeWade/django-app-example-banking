# Generated by Django 2.2.6 on 2019-10-22 02:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20191021_2226'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='certificatedeposit',
            options={'verbose_name_plural': 'CDs'},
        ),
        migrations.AlterModelOptions(
            name='certificatedepositira',
            options={'verbose_name_plural': 'IRA CDs'},
        ),
    ]
