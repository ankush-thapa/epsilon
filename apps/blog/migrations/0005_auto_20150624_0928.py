# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_writer_domain_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='writer',
            name='blog_meta_description',
            field=models.CharField(default=datetime.datetime(2015, 6, 24, 9, 28, 29, 544511), max_length=300, db_column=b'blog_meta_description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='writer',
            name='blog_meta_keywords',
            field=models.CharField(default=datetime.datetime(2015, 6, 24, 9, 28, 38, 228979), max_length=500, db_column=b'blog_meta_keywords'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='writer',
            name='blog_meta_title',
            field=models.CharField(default=datetime.datetime(2015, 6, 24, 9, 28, 43, 961359), max_length=150, db_column=b'blog_meta_title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='writer',
            name='blog_tagline',
            field=models.CharField(default=datetime.datetime(2015, 6, 24, 9, 28, 50, 497368), max_length=100, db_column=b'blog_tagline'),
            preserve_default=False,
        ),
    ]
