# Generated by Django 3.2.4 on 2021-06-26 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuesta', '0003_remove_poll_texto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuestion1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('texto', models.TextField(blank=True)),
            ],
        ),
    ]
