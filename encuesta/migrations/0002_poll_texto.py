# Generated by Django 3.2.4 on 2021-06-26 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuesta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='texto',
            field=models.TextField(blank=True),
        ),
    ]
