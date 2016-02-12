pyunpian - Yunpian Python SDK
-----
* Quck Install
```
wget https://raw.githubusercontent.com/shenjinti/pyunpian/master/pyunpian.py

python pyunpian.py -h
```
Or via `pip`
```
pip install https://github.com/shenjinti/pyunpian/archive/master.zip
python -m pyunpian -h
```

* Basic Usage:    

Send SMS text:  
```
python pyunpian.py -k YOUR-KEY -m 18078901234 -t YOUR-TEXT

```

Send `Code` voice via phone call:
```
python pyunpian.py -k YOUR-KEY -m 18078901234 -c CODE
```

Get Account info   
```
python pyunpian.py -k YOUR-KEY -u
```
