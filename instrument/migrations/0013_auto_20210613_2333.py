# Generated by Django 3.2 on 2021-06-13 23:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instrument', '0012_auto_20210613_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrument',
            name='profiles',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='instrument',
            name='region',
            field=models.CharField(choices=[('Independent', 'Independent'), ('Europe', 'Europe'), ('Africa', 'Africa'), ('United States', 'United States'), ('Asia', 'Asia'), ('Russia', 'Russia')], max_length=13),
        ),
        migrations.AlterField(
            model_name='instrument',
            name='sector',
            field=models.CharField(choices=[('Precious Metals', 'Precious Metals'), ('Energy', 'Energy'), ('Metals', 'Metals'), ('Equity', 'Equity'), ('Cash', 'Cash')], max_length=15),
        ),
        migrations.DeleteModel(
            name='Region',
        ),
        migrations.DeleteModel(
            name='Sector',
        ),
    ]
