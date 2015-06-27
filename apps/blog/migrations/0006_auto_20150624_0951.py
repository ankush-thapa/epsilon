# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150624_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='writer',
            name='facebook_link',
            field=models.CharField(default=datetime.datetime(2015, 6, 24, 9, 51, 19, 540848), max_length=100, db_column=b'facebook_link'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='writer',
            name='gplus_link',
            field=models.CharField(default=datetime.datetime(2015, 6, 24, 9, 51, 25, 53349), max_length=100, db_column=b'gplus_link'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='writer',
            name='twitter_link',
            field=models.CharField(default=datetime.datetime(2015, 6, 24, 9, 51, 30, 167654), max_length=100, db_column=b'twitter_link'),
            preserve_default=False,
        ),
    ]
