# Generated by Django 3.0.4 on 2020-04-28 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailytask', '0002_dailytask_remark'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailytask',
            name='totalHours',
            field=models.IntegerField(null=True),
        ),
    ]
