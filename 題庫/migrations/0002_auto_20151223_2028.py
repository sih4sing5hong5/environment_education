# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('題庫', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='作答紀錄表',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('作答時間', models.DateTimeField(auto_now_add=True)),
                ('總題數', models.IntegerField()),
                ('答錯題數', models.IntegerField()),
                ('答錯題目', models.CharField(max_length=20000)),
                ('答對題目', models.CharField(max_length=20000)),
                ('xls檔案', models.ForeignKey(to='題庫.xls檔案表')),
            ],
        ),
        migrations.CreateModel(
            name='使用者表',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='作答紀錄表',
            name='使用者',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='作答紀錄'),
        ),
    ]
