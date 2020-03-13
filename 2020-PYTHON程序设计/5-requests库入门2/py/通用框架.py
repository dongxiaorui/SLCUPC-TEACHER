import requests

def getHtmlText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        if "机器人" in r.text:
            return "异常"
        return r.text
    except:
        return "异常"

if __name__ == '__main__':
    url="http://www.baidu.com"
    print(getHtmlText(url))

