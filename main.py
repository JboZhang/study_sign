import requests
import re
from bs4 import BeautifulSoup
import json
import os, sys

os.chdir(sys.path[0])

headers = {
    'Accept-Encoding':
    'gzip, deflate, br',
    'Accept-Language':
    'zh,zh-CN;q=0.9,zh-TW;q=0.8',
    'Cookie':
    your cookie,
    'User-Agent':
    'your User-Agent'
}

Class_params = [{
    'name': '签到课程:你的课程名',
    'courseId': 你的courseld,
    'jclassId': 你的jclassd
}, {
    上同
}, {
    上同
}]
with open("only.json", 'r', encoding='utf-8') as f:
    dic = json.load(f)
url = 'https://mobilelearn.chaoxing.com/widget/pcpick/stu/index'
for val in Class_params:
    if dic[val['courseId']]:
        continue
    html = requests.get(url, headers=headers, params=val)
    fid = re.findall('<input type="hidden" id="fid" value="(.*?)" />',
                     html.text, re.S)
    soup = BeautifulSoup(html.text, 'html.parser')
    html = str(soup.find('div', id="startList"))
    activeId = re.findall(
        '<div class="Mct" onclick="activeDetail[(](.*?),2,null[)]">', html,
        re.S)
    if activeId:
        params = {
            'activeId': activeId[0],
            'classId': val['jclassId'],
            'fid': fid[0],
            'courseId': val['courseId']
        }
        url_q = 'https://mobilelearn.chaoxing.com/widget/sign/pcStuSignController/preSign'
        html = requests.get(url_q, headers=headers, params=params)
        text = '签到通知!'
        desp = ''
        i = 0
        if '签到成功' in html.text:
            name = re.findall('<a href="javascript:;" shape="rect">(.*?)</a>',
                              html.text, re.S)
            Time = re.findall('<em id="st">(.*?)</em></dd>', html.text, re.S)
            desp = desp + '```' + val['name'] + '``` '
            i = i + 1
            desp = desp + '```签到标题:' + name[1] + '``` '
            desp = desp + '```签到状态:' + 'Success``` '
            desp = desp + '```签到时间:' + Time[0] + '```'
            params = {'text': text, 'desp': desp}
            requests.get(
                'https://sc.ftqq.com/你的个人API链接.send',
                params=params)
            dic[val['courseId']] = True
with open("only.json", 'w', encoding='utf-8') as f:
    f.write(json.dumps(dic, ensure_ascii=False, indent=4))
