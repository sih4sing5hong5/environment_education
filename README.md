# 環境教育擂臺題庫
方便練習題庫

## 使用方法
###環境
```bash
sudo apt-get install -y python3 python-virtualenv # Ubuntu/Mint 安裝指令
virtualenv venv --python python3 # 設置環境檔
. venv/bin/activate # 載入環境
pip install -r requirements.txt
```

### 初使化資料庫
```bash
python manage.py migrate
```

### 匯入資料
```bash
python manage.py shell
```
輸入
```python
from django.core.files.base import File
from 題庫.models import xls檔案表
檔案所在 = '8-1-環保知識挑戰擂台賽.xls'
with open(檔案所在, 'rb') as 檔案:
    xls檔案表.匯入xls(File(檔案))
```

### FB登入
```
```

## 授權
本專案用MIT License.

## 聯絡資訊

有事請聯絡草湖國中 鄭主任 04-8861051#218