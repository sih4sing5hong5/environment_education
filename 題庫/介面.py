
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from 題庫.models import xls檔案表
from 題庫.models import 作答紀錄表


@login_required(login_url='/accounts/facebook/login')
def 練習(request):
    網址 = '題庫/作答.html'
    return render(request, 網址, {
        '題目陣列': xls檔案表.上新的檔案().隨機揀題號()
    })

@login_required(login_url='/accounts/facebook/login')
def 送出答案(request):
    xls檔案 = xls檔案表.上新的檔案()
    答對 = []
    答錯 = []
    for (題號, 選的答案) in _提出題號佮答案(request.POST):
        if xls檔案.題號(題號).答案 == int(選的答案):
            答對.append(題號)
        else:
            答錯.append(題號)
    作答紀錄表.試驗結果(request.user, xls檔案, 答錯, 答對)
    return redirect('看作答紀錄')

@login_required(login_url='/accounts/facebook/login')
def 看作答紀錄(request):
    網址 = '題庫/作答結果.html'
    return render(request, 網址, {
        '作答紀錄陣列': 作答紀錄表.揣出作答紀錄(request.user),
    })

@login_required(login_url='/accounts/facebook/login')
def 看解釋(request, 題號):
    xls檔案 = xls檔案表.上新的檔案()
    網址 = '題庫/解釋.html'
    return render(request, 網址, {
        '題目': xls檔案.題號(題號),
    })


def _提出題號佮答案(POST):
    for 第幾個 in range(xls檔案表.揀題目數量):
        try:
            題號 = POST['id[{}]'.format(第幾個)]
        except:
            題號 = -1
        try:
            選的答案 = POST['ans[{}]'.format(第幾個)]
        except:
            選的答案 = -1
        yield (題號, 選的答案)
