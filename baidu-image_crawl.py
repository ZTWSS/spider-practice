import requests
from fake_useragent import FakeUserAgent
import time
import json
import jsonpath
import re

def get_respose(url_):
    headers_ = {'User-Agent':FakeUserAgent().random}
    return requests.get(url=url_,headers=headers_)

url_ = input('请输入要爬取百度图片的异步响应文件的url：')
num = int(input('请输入爬取的页数：'))
lurl = re.findall('(.*)&pn=(.*?)&rn=(.*?)&(.*)',url_)

pngUrlList = []

i = 0
while i < num:
    respose_ = get_respose(lurl[0][0]+'&pn='+str(int(lurl[0][1])+i*int(lurl[0][2]))+'&rn='+lurl[0][2]+lurl[0][3])
    pngUrls = jsonpath.jsonpath(json.loads(respose_.text),'$..data..thumbURL')
    pngUrlList.extend(pngUrls)
    i+=1
    time.sleep(1)
    print('成 功 获 取 %d 页！'%i)

count = 1
for pngUrl in pngUrlList:
    oneRespose_ = get_respose(pngUrl)
    with open('./images/pic%02d.png'%count,'wb') as f:
        f.write(oneRespose_.content)
        print('第%d张图片获取成功！'%count)
    count +=1
    time.sleep(0.5)


