from lxml import etree
import requests

music_name = '青花瓷'
index_url = r'''https://www.kugou.com/song/#hash=3D1881ABB3078304FB151503EB6B1D33&album_id=965453'''.format(music=music_name)
response = requests.post(index_url)
content = response.content.decode()
content_html = etree.HTML(content)
music = content_html.xpath('//div@[class="g-bd"]//div@[class="g-wrap n-srch"]//div@[class]//div@[class="item f-cb h-flag  "]')
response = requests.get('https://music.163.com/#/search/m/?s="music"')
print(response.text)


