# Generated by Django 3.2 on 2021-05-28 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(default='coding', max_length=120),
        ),
    ]