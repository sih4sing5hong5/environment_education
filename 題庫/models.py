# -*- coding: utf-8 -*-
from datetime import datetime
from django.conf.global_settings import MEDIA_ROOT
from django.contrib.auth.models import User
from django.db import models
import json
from os.path import join
from random import randint
import xlrd


class xls檔案表(models.Model):
    xls檔案 = models.FileField()
    收錄時間 = models.DateTimeField(auto_now_add=True)
    揀題目數量 = 80

    @classmethod
    def 匯入xls(cls, xls檔案, 名=None):
        if 名 is None:
            名 = '{}.xls'.format(
                datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            )
        資料 = xls檔案表.objects.create()
        資料.xls檔案.save(名, xls檔案)
        資料.匯入題目()
        return 資料

    @classmethod
    def 上新的檔案(cls):
        return cls.objects.all().order_by('-收錄時間').first()

    def 匯入題目(self):
        表格檔 = xlrd.open_workbook(join(MEDIA_ROOT, self.xls檔案.path))
        表格 = 表格檔.sheet_by_index(0)
        表格欄位 = {}
        for 第幾個, 資料 in enumerate(表格.row_values(0)):
            表格欄位[資料] = 第幾個
        for 第幾逝 in range(1, 表格.nrows):
            題目表.加題目(self, 第幾逝, 表格欄位, 表格.row_values(第幾逝))

    def 隨機揀題號(self):
        題目數量 = self.題目.count()
        題目陣列 = []
        for _ in range(self.揀題目數量):
            題號 = randint(1, 題目數量)
            題目陣列.append(self.題目.get(題號=題號))
        return 題目陣列

    def 題號(self, 題號):
        return self.題目.get(題號=題號)


class 題目表(models.Model):
    長度 = 10000
    xls檔案 = models.ForeignKey(xls檔案表, related_name='題目')
    題號 = models.IntegerField()
    級別 = models.CharField(max_length=20)
    題目 = models.CharField(max_length=長度)
    選項1 = models.CharField(max_length=長度)
    選項2 = models.CharField(max_length=長度)
    選項3 = models.CharField(max_length=長度)
    選項4 = models.CharField(max_length=長度)
    答案 = models.IntegerField()
    解析 = models.CharField(max_length=長度)

    @classmethod
    def 加題目(cls, xls檔案, 題號, 表格欄位, 資料):
        return 題目表.objects.create(
            xls檔案=xls檔案,
            題號=題號,
            級別=資料[表格欄位['級別']],
            題目=資料[表格欄位['題目']],
            選項1=資料[表格欄位['選項1']],
            選項2=資料[表格欄位['選項2']],
            選項3=資料[表格欄位['選項3']],
            選項4=資料[表格欄位['選項4']],
            答案=資料[表格欄位['答案']],
            解析=資料[表格欄位['解析']],
        )


class 使用者表(User):

    class Meta:
        proxy = True


class 作答紀錄表(models.Model):
    使用者 = models.ForeignKey(User, related_name='作答紀錄')
    xls檔案 = models.ForeignKey(xls檔案表)
    作答時間 = models.DateTimeField(auto_now_add=True)
    總題數 = models.IntegerField()
    答錯題數 = models.IntegerField()
    答錯題目 = models.CharField(max_length=20000)
    答對題目 = models.CharField(max_length=20000)

    @classmethod
    def 試驗結果(cls, 使用者, xls檔案, 答錯題目, 答對題目):
        return cls.objects.create(
            使用者=使用者,
            xls檔案=xls檔案,
            總題數=len(答對題目) + len(答錯題目),
            答錯題數=len(答錯題目),
            答對題目=json.dumps(答對題目),
            答錯題目=json.dumps(答錯題目),
        )

    @classmethod
    def 揣出作答紀錄(cls, 使用者):
        return cls.objects.filter(
            使用者=使用者,
            xls檔案=xls檔案表.上新的檔案(),
        ).order_by('-作答時間')

    def 答錯題目陣列(self):
        return json.loads(self.答錯題目)

    def 答對題目陣列(self):
        return json.loads(self.答對題目)
