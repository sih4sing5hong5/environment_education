from os.path import join

from django.conf import settings
from django.core.files.base import File
from django.http.response import HttpResponsePermanentRedirect
from django.test.testcases import TestCase


from 題庫.models import xls檔案表


class 作答試驗(TestCase):

    @classmethod
    def setUpClass(cls):
        super(cls, cls).setUpClass()
        檔案所在 = join(settings.BASE_DIR, '8-1-環保知識挑戰擂台賽.xls')
        with open(檔案所在, 'rb') as 檔案:
            cls.檔案 = xls檔案表.匯入xls(File(檔案))

    def test_愛登入(self):
        回應 = self.client.post('/練習')
        self.assertIsInstance(回應, HttpResponsePermanentRedirect)
