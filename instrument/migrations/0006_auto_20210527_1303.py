# Generated by Django 3.2 on 2021-05-27 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instrument', '0005_instrument_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrument',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='instrument',
            name='region',
            field=models.CharField(choices=[('In', 'Independent'), ('EU', 'Europe'), ('Af', 'Africa'), ('US', 'United States'), ('AS', 'Asia'), ('Rus', 'Russia')], max_length=3),
        ),
        migrations.AlterField(
            model_name='instrument',
            name='stake',
            field=models.CharField(choices=[('pm', 'Precious Metals'), ('Eg', 'Energy'), ('Met', 'Metals'), ('Eq', 'Equity'), ('Cs', 'Cash')], max_length=3),
        ),
        migrations.AlterField(
            model_name='instrument',
            name='total_price',
            field=models.FloatField(blank=True),
        ),
    ]
