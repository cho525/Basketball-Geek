# Generated by Django 4.2 on 2023-04-24 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamestats', '0010_lastupdate_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamcache',
            name='ast',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='teamcache',
            name='ftd',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='teamcache',
            name='orb',
            field=models.CharField(max_length=10),
        ),
    ]
