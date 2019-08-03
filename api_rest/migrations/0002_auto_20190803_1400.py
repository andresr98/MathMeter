# Generated by Django 2.2.3 on 2019-08-03 19:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api_rest.Teacher'),
        ),
        migrations.AddField(
            model_name='exam',
            name='duration',
            field=models.IntegerField(default=60),
        ),
        migrations.AddField(
            model_name='studentanswer',
            name='date',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
    ]
