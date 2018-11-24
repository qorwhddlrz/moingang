# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(50000), django.core.validators.MaxValueValidator(1000000000)]),
        ),
    ]
