# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_category_slug1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='slug1',
            field=models.SlugField(),
            preserve_default=True,
        ),
    ]
