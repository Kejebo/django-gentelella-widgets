# Generated by Django 3.1 on 2020-09-18 15:17

import demoapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0008_auto_20200916_1352'),
    ]

    operations = [
        migrations.CreateModel(
            name='Multiwidget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=14, validators=[demoapp.models.validate_inputs])),
                ('date', models.DateField()),
            ],
        ),
    ]