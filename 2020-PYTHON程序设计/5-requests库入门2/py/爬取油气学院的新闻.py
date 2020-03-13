import 通用框架
import re
import time
#以正则方式进行文字提取

def getUrl(i):
    if i==50:
        return "http://yqxy.slcupc.edu.cn/index/xyxw.htm"
    else:
        return "http://yqxy.slcupc.edu.cn/index/xyxw/"+str(i)+".htm"

if __name__ == '__main__':
    for i in range(50,0,-1):
        url=getUrl(i)
        html=通用框架.getHtmlText(url)
        fs = re.findall(r'<a href="(.*?)">\r\n<span>(.*?)</span>(.*?)</a>', html)
        for f in fs:
            if "培训" in f[2]:
                print(f)
        time.sleep(1)