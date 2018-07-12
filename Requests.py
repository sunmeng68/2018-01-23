# -*- coding: utf-8 -*-

import requests

#访问一个页面
r=requests.get('https://book.douban.com/author/4502361/')
print(r.status_code)  # 打印状态码
#print(r.url)          # 打印请求url
#print(r.headers)      # 打印头信息
#print(r.cookies)      # 打印cookie信息
#print(r.text)  #以文本形式打印网页源码
#print(r.content) #以字节流形式打印

#对于带参数的url，传入一个dict作为params参数
#例：https://www.douban.com/search?q=python&cat=1001
r2=requests.get('https://www.douban.com/search',params={'q':'python','cat':'1001'})
print (r2.url)
#对于特定类型的响应，例如JSON，可以直接获取
r3 = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
print (r3.json())
#需要传入HTTP Header时，我们传入一个dict作为headers参数
r4 = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
print (r4.url)
#post,只需要把get()方法变成post()，然后传入data参数作为POST请求的数据
r5 = requests.post('https://accounts.douban.com/login', data={'form_email': '1019378099@qq.com', 'form_password': '960608sm'})
print (r5.url)