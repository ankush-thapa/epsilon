# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150624_0852'),
    ]

    operations = [
        migrations.AddField(
            model_name='writer',
            name='blog_name',
            field=models.CharField(default=datetime.datetime(2015, 6, 24, 8, 55, 59, 560374), max_length=100, db_column=b'blog_name'),
            preserve_default=False,
        ),
    ]
