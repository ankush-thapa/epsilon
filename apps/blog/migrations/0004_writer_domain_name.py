# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_writer_blog_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='writer',
            name='domain_name',
            field=models.CharField(default=datetime.datetime(2015, 6, 24, 9, 12, 54, 442469), max_length=100, db_column=b'domain_name'),
            preserve_default=False,
        ),
    ]
