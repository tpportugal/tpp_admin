# Generated by Django 2.0 on 2018-02-25 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stops', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stop',
            name='place',
        ),
    ]