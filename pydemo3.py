# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# import requests
# from bs4 import BeautifulSoup
# import urllib2 
# url="https://www.52cp.cn/h5/cqssc?t=1587009251783"
# import requests
# # url="http://www.cnblogs.com/hjw1"
# ua={"user-agent":"Mozilla/5.0"}
# # r=requests.get(url)
# # print r.request.headers  
# r=requests.get(url,headers=ua)
# # print r.request.headers  
# # 修改头信息可模仿浏览器访问
# # print r.text
# soup = BeautifulSoup(r.text,fromEncoding="gb18030")
# print soup.prettify()

# 请求库
import requests
# 解析库
from bs4 import BeautifulSoup
# 用于解决爬取的数据格式化
import io
import sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
# 爬取的网页链接
# ua={"user-agent":"Mozilla/5.0"}
# r= requests.get("https://www.52cp.cn/h5/cqssc?t=1587009251783",headers=ua)
# 类型
# print(type(r))
# print(r.status_code)
# 中文显示
# r.encoding='utf-8'
# print(r.encoding)
# print(r.text)
# result = r.text
# print result
# 再次封装，获取具体标签内的内容
# bs = BeautifulSoup(result,'html.parser')
# print bs
# bs = BeautifulSoup(r.text)
# 具体标签
# print("解析后的数据")
# print(bs.span)
# a={}
# 获取已爬取内容中的script标签内容
# data=bs.find_all('script')
# 获取已爬取内容中的td标签内容
# data1=bs.select('tr') 
# data1=bs.find_all('tr')
# print bs.prettify()
# 循环打印输出
# print data1
# for i in data:
#     a=i.text
#     print(i.text)
# for j in data1:
#     print(j.text)