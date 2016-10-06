from django.conf.urls import patterns, url


from 題庫.介面 import 練習
from 題庫.介面 import 送出答案
from 題庫.介面 import 看解釋
from 題庫.介面 import 看作答紀錄
from 題庫.介面 import 搶答題目
from 題庫.介面 import 送出搶答

urlpatterns = patterns(
    '',
    url(r'^練習', 練習, name='練習'),
    url(r'^送出答案$', 送出答案),
    url(r'^看解釋/(?P<題號>\d+)$', 看解釋, name='看解釋'),
    url(r'^搶答題目', 搶答題目),
    url(r'^送出搶答', 送出搶答),    

    url(r'^$', 看作答紀錄, name='看作答紀錄'),
)
