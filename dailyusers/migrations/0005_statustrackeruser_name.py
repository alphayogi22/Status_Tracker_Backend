# Generated by Django 3.0.4 on 2020-04-28 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailyusers', '0004_statustrackeruser_leavebalance'),
    ]

    operations = [
        migrations.AddField(
            model_name='statustrackeruser',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
