# Generated by Django 2.2.6 on 2019-10-20 19:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('minimum', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile')),
            ],
        ),
        migrations.AlterField(
            model_name='certificatedeposit',
            name='minimum',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='certificatedepositira',
            name='minimum',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='moneymarket',
            name='minimum',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='savings',
            name='minimum',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
        migrations.DeleteModel(
            name='Checkings',
        ),
    ]
