import 通用框架
import time
'''
import requests
r = requests.get("http://jcxy.slcupc.edu.cn/info/1155/2532.htm")
r.encoding=r.apparent_encoding #r.apparent_encoding，通过网页内容去推断编码形式
print(r.text)
'''
url="http://jcxy.slcupc.edu.cn/info/1155/2532.htm"
html=通用框架.getHtmlText(url)
if html =="异常":
    time.sleep(30)
else:
    print(html)
