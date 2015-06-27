# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150624_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='header_image',
            field=models.ImageField(null=True, upload_to=b'static/images/', db_column=b'header_image', blank=True),
        ),
        migrations.AlterField(
            model_name='publicimage',
            name='image',
            field=models.ImageField(null=True, upload_to=b'static/images/', db_column=b'header_image', blank=True),
        ),
        migrations.AlterField(
            model_name='writer',
            name='cover_image',
            field=models.ImageField(null=True, upload_to=b'static/images/', db_column=b'cover_image', blank=True),
        ),
    ]
