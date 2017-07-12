# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-06 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RSR', '0002_auto_20170703_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='wordstr',
            field=models.CharField(default=1, max_length=5000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ocr',
            name='Resume',
            field=models.FileField(upload_to='\\PreOCR'),
        ),
        migrations.AlterField(
            model_name='person',
            name='Resume',
            field=models.FileField(upload_to='\resumes'),
        ),
        migrations.AlterField(
            model_name='person_company',
            name='EndDate',
            field=models.DateField(default=6, verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='person_company',
            name='StartDate',
            field=models.DateField(default=6, verbose_name='Start Date'),
        ),
    ]
