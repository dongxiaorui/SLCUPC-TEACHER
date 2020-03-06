#访问百度
import requests

r=requests.get("http://www.baidu.com")
r.encoding = r.apparent_encoding
print(r.text)