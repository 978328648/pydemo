# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# import requests
# import re
# from bs4 import BeautifulSoup
# from lxml import html
# def main():
#     url = "https://www.52cp.cn/h5/cqssc?t=1587009251783"
#     get_content(url)

# def get_html_text(url):
#     try:
#         ua={"user-agent":"Mozilla/5.0"}
#         r = requests.get(url,timeout=30,headers=ua)
#         r.encoding = 'utf-8'    # 编码方式
#         return r.text
#     except BaseException as e:
#         print('BaseException:', e)
#         return ""

# def get_content(url):
#     html = get_html_text(url)
    
#     soup = BeautifulSoup(html, 'lxml',from_encoding="gb18030")
#     links=soup.find_all('tr')
#     for index1 in links:
#         # print type(index1)
#         a = index1.find_all('td')
#         print a[0]
        
    


# main()
