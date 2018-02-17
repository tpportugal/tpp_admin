# Generated by Django 2.0 on 2018-02-15 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday', models.SmallIntegerField(default=0)),
                ('tuesday', models.SmallIntegerField(default=0)),
                ('wednesday', models.SmallIntegerField(default=0)),
                ('thursday', models.SmallIntegerField(default=0)),
                ('friday', models.SmallIntegerField(default=0)),
                ('saturday', models.SmallIntegerField(default=0)),
                ('sunday', models.SmallIntegerField(default=0)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
    ]