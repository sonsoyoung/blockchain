# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('isbn', models.BigIntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('memo', jsonfield.fields.JSONField(default={})),
            ],
        ),
    ]
