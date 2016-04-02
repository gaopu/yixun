#!/usr/bin/python
#coding:utf-8
import os
import urllib2
from urllib import quote

acc = '用户名'
pwd = '密码'

# 运行算法计算结果并返回给ｘ
p = os.popen('./yixun ' + acc)
x = p.read()
p.close()

print "算法结果：" + x

url = "http://192.168.1.1/userRpm/PPPoECfgRpm.htm?wan=0&wantype=2&acc=%0D%0A"+x+"&psw="+pwd+"&confirm="+pwd+"&specialDial=100&SecType=0&sta_ip=0.0.0.0&sta_mask=0.0.0.0&linktype=2&Save=%B1%A3+%B4%E6"
print "请求链接：" + url

request = urllib2.Request(url)
request.add_header("Cookie","Authorization=Basic%20YWRtaW46aHVxaWFuZ3hp; ChgPwdSubTag=")
request.add_header("Referer","http://192.168.1.1/userRpm/PPPoECfgRpm.htm")
urllib2.urlopen(request)