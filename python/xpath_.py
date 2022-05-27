# from lxml import etree
# import bs4
# import requests
# import re
# from urllib.parse import urljoin
# BASE_URL = 'http://www.xs5200.com/'
# # 高数  数据结构  算法 矩阵（线性代数） 概率论   英语雅思
# # response = requests.post(BASE_URL)
# # content = response.content.decode()
# # content_html = etree.HTML(content)
# # content_list = content_html.xpath('//div@id="wrapper"//div')
#
# response = requests.get(BASE_URL)
# #print(response.text)
# # print(type(response.text))
# lists = re.findall('<dl><dt><a href=\"http://www.xs5200.com/.*/\">.*</a></dt><dd>',response.text)
# for i in lists:
#     print(i)
# for i in lists:
#     str1 = re.findall('http://www.xs5200.com/.*?<',i)[0]
#     str1 = str1[:-1]
#     str1 = str1.replace('\">', ' ')
#     print(str1)
import re
import codecs
import bs4
import requests

# url = 'http://www.xs5200.com//77_77762/32059522.html'
# response = requests.get(url)
# soup = bs4.BeautifulSoup(response.content, 'lxml')
# s = re.findall('<div id=\"content\">.*</div>', str(soup))[0]
# s = s.replace('<div id=\"content\">    ', '')
# s = s.replace('</div>', '')
# s = s.replace('<br/><br/>    ', '\n')
# print(s)
# fp = codecs.open('0.txt', 'w',encoding='utf-8')
# fp.write(s)
# fp.close()
# url = 'http://www.xs5200.com//77_77762/32059523.html'
# response = requests.get(url)
# soup = bs4.BeautifulSoup(response.content,'lxml')
# #print(soup)
# a = re.findall('<div id="content"> .*</div>',str(soup))[0]
# #print(a)
# a = a.replace('<div id="content">    ','')
# a = a.replace('</div>','')
# a = a.replace('<br/><br/>    ','\n')
# print(a)
# b = codecs.open('b.txt','w',encoding='utf-8')
# b.write(a)
# b.close()
       #A   节点宽度为
   #b      c
  #d e    f  g ->href='xxx'
  #//A/c/g@href    O(1)
  # ABD Abe Acf Acg  O(n^2)



















