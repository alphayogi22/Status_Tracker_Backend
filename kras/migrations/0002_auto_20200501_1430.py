# Generated by Django 3.0.4 on 2020-05-01 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kras', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kra',
            name='endDate',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='kra',
            name='startDate',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='kra',
            name='thresholdStatus',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='kra',
            name='year',
            field=models.IntegerField(blank=True),
        ),
    ]
