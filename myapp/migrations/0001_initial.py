# Generated by Django 3.0.2 on 2020-02-01 23:40

import django.contrib.postgres.fields.hstore
from django.contrib.postgres.operations import HStoreExtension
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        HStoreExtension(),
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=66)),
                ('metadata', django.contrib.postgres.fields.hstore.HStoreField(blank=True)),
            ],
        ),
    ]
