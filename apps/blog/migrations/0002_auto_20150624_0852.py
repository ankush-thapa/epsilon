# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='writer',
            name='cover_image',
            field=models.ImageField(null=True, upload_to=b'staticfiles/images/', db_column=b'cover_image', blank=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='header_image',
            field=models.ImageField(null=True, upload_to=b'staticfiles/images/', db_column=b'header_image', blank=True),
        ),
        migrations.AlterField(
            model_name='publicimage',
            name='image',
            field=models.ImageField(null=True, upload_to=b'staticfiles/images/', db_column=b'header_image', blank=True),
        ),
    ]
