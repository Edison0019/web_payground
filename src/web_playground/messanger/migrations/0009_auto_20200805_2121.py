# Generated by Django 3.0.8 on 2020-08-06 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messanger', '0008_thread_updated'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='thread',
            options={'ordering': ['-updated']},
        ),
    ]
