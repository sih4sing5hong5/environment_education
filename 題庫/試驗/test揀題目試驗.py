from os.path import join

from django.conf import settings
from django.core.files.base import File
from django.test.testcases import TestCase


from 題庫.models import xls檔案表


class 揀題目試驗(TestCase):

    @classmethod
    def setUpClass(cls):
        super(cls, cls).setUpClass()
        檔案所在 = join(settings.BASE_DIR, '8-1-環保知識挑戰擂台賽.xls')
        with open(檔案所在, 'rb') as 檔案:
            cls.檔案 = xls檔案表.匯入xls(File(檔案))

    def test_隨機揀題號(self):
        第一擺揀著的 = self.檔案.隨機揀題號()
        第二擺揀著的 = self.檔案.隨機揀題號()
        self.assertNotEqual(第一擺揀著的, 第二擺揀著的)

    def test_揀題號結果是陣列(self):
        self.assertIsInstance(self.檔案.隨機揀題號(), list)
