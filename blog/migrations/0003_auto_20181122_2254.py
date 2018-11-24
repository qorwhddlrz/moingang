# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='price',
            field=models.CharField(max_length=10, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='teacherName',
            field=models.CharField(max_length=10, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
