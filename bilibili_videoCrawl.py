import requests
from fake_useragent import FakeUserAgent
from lxml import html
import re
from moviepy.editor import *
import os
import time

# 在b站网页获取视频播放时的url即可
try:
    start = time.time()
    url_ = input('请输入b站视频页面url：')

    headers_ = {
        'User-Agent': FakeUserAgent().random,
        'referer': 'https://search.bilibili.com/all?keyword=%E7%A5%9E%E4%BB%99%E9%A2%9C%E5%80%BC%EF%BC%81%E8%B6%85%E7%BE%8E%E4%BF%84%E5%9B%BD%E5%B0%8F%E5%A7%90%E5%A7%90-Dasha+taran!&from_source=webtop_search&spm_id_from=333.1007'
    }

    respose_ = requests.get(url=url_, headers=headers_)

    html_data = html.etree.HTML(respose_.text)

    parse_html = str(html_data.xpath("//script[contains(text(),'window.__playinfo__')]/text()"))

    title_video = str(html_data.xpath("//title/text()"))
    title_video = re.sub('[/&]', '', title_video)

    video_url = re.findall('''"video":\[{"id":80,"baseUrl":"(.*?)"''', parse_html)[0]
    audio_url = re.findall('''"audio":\[{"id":30280,"baseUrl":"(.*?)"''', parse_html)[0]

    resposev_ = requests.get(url=video_url, headers=headers_)
    resposea_ = requests.get(url=audio_url, headers=headers_)
    with open('./video.mp4', 'wb') as f:
        f.write(resposev_.content)
    with open('./audio.mp3', 'wb') as f:
        f.write(resposea_.content)
    ffmpeg_tools.ffmpeg_merge_video_audio('./video.mp4', './audio.mp3', f'./{title_video}.mp4')

    os.remove('./video.mp4')
    os.remove('./audio.mp3')
    end = time.time()
except Exception as e:
    print('出现异常！',e)
else:
    print('下载完成！，文件大小为：%.2fMB'%(os.path.getsize(f'./{title_video}.mp4')/1024/1024))
    print(f'用时：{end-start}')
finally:
    print('欢迎下次使用！')

