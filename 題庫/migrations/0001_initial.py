# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='xls檔案表',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('xls檔案', models.FileField(upload_to='')),
                ('收錄時間', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='題目表',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('題號', models.IntegerField()),
                ('級別', models.CharField(max_length=20)),
                ('題目', models.CharField(max_length=10000)),
                ('選項1', models.CharField(max_length=10000)),
                ('選項2', models.CharField(max_length=10000)),
                ('選項3', models.CharField(max_length=10000)),
                ('選項4', models.CharField(max_length=10000)),
                ('答案', models.IntegerField()),
                ('解析', models.CharField(max_length=10000)),
                ('xls檔案', models.ForeignKey(related_name='題目', to='題庫.xls檔案表')),
            ],
        ),
    ]
