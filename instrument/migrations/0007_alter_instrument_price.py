# Generated by Django 3.2 on 2021-05-27 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instrument', '0006_auto_20210527_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrument',
            name='price',
            field=models.FloatField(),
        ),
    ]
