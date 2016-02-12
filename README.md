pyunpian - Yunpian Python SDK
-----
* Quck Install
```
wget https://github.com/shenjinti/pyunpian/blob/master/pyunpian.py

python pyunpian.py -h
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
