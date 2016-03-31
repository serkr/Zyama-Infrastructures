# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structures', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='structure',
            name='name',
            field=models.CharField(default='123', max_length=200),
            preserve_default=False,
        ),
    ]
