# Generated by Django 3.2 on 2021-06-13 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instrument', '0010_auto_20210613_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrument',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='instrument.region'),
        ),
        migrations.AlterField(
            model_name='instrument',
            name='sector',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='instrument.sector'),
        ),
    ]
