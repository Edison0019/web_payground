# Generated by Django 3.0.8 on 2020-07-30 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messanger', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date'),
        ),
    ]
