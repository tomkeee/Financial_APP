# Generated by Django 3.2 on 2021-05-24 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instrument', '0002_instrument_profiles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=10)),
            ],
        ),
    ]
