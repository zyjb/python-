import requests
url = 'https://www.sogou.com/web'
#处理url携带的参数进行处理：封装到字典中
kw = input('enter a word；')
# 计算机网络  主要是协议
# 操作系统原理 c语言  指针
# 密码学  数学 无监督人工智能

#对指定的url发起的请求对于的url是携带参数的，并且请求过程中处理的参数
response = requests.get(url = url)
page_text = response.text
fileName = 'kw+.html'
with open(fileName+'txt','w',encoding= 'utf-8') as fp:
    fp.write(page_text)
    print(fileName,'保存成功！！!')