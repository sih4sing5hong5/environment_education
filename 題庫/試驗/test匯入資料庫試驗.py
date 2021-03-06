from os.path import join

from django.conf import settings
from django.core.files.base import File
from django.test.testcases import TestCase


from 題庫.models import xls檔案表
from 題庫.models import 題目表


class 匯入資料庫試驗(TestCase):

    @classmethod
    def setUpClass(cls):
        super(cls, cls).setUpClass()
        檔案所在 = join(settings.BASE_DIR, '8-1-環保知識挑戰擂台賽.xls')
        with open(檔案所在, 'rb') as 檔案:
            cls.檔案 = xls檔案表.匯入xls(File(檔案))

    def test_匯入xls資料檢查檔案(self):
        self.assertEqual(xls檔案表.objects.all().count(), 1)

    def test_匯入xls資料檢查題目(self):
        self.assertEqual(題目表.objects.all().count(), 5688)
