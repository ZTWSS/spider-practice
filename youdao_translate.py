import random
import requests
from fake_useragent import FakeUserAgent
import json
import jsonpath
import hashlib
import time

while True:
    keyWords_ = input('请输入要翻译的文字：')

    url_ = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    headers_ = {
        'User-Agent': FakeUserAgent().random,
        'Referer': 'https://fanyi.youdao.com/',
        'Cookie': 'OUTFOX_SEARCH_USER_ID=1710039446@10.110.96.154; OUTFOX_SEARCH_USER_ID_NCOO=1907941232.2706099; JSESSIONID=aaaCJLWwWZOnagI2tK5_x; ___rl__test__cookies=1648085807884'
    }

    time_ = str(int(time.time() * 1000))

    salt_ = time_ + str(random.randint(0, 9))

    sign_ = hashlib.md5(("fanyideskweb" + keyWords_ + salt_ + "Ygy_4c=r#e#4EX^NUGUc5").encode()).hexdigest()
    data_ = {
        'i': keyWords_,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt_,
        'sign': sign_,
        'lts': time_,
        'bv': 'a6b36904bd1a38729b798f9a67c14dd9',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
    }

    try:
        respose_ = requests.post(url=url_, headers=headers_, data=data_)

        jsonData_py = json.loads(respose_.text)

        result_ = jsonpath.jsonpath(jsonData_py, '$..translateResult..tgt')

        print('翻译结果为：' + result_[0])
    except Exception as e:
        print(e, '输入有误！', '请重新输入！')
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    else:
        print('----------------------------------------')
