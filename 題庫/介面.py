from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from 題庫.models import xls檔案表

@login_required(login_url='/accounts/facebook/login')
def 練習(request):
    網址='題庫/作答.html'
    return render(request, 網址, {
        '題目陣列': xls檔案表.上新的檔案().隨機揀題號()
    })