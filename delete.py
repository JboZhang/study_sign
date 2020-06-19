import json, os, sys

os.chdir(sys.path[0])

dic = {
    "你的课程码": False,
    "你的课程码":False,
    "你的课程码":False,
    "你的课程码":False,
    "你的课程码":False,
    "你的课程码":False,
    "你的课程码":False,
    "你的课程码":False,
    "你的课程码":False
}

with open("/home/bobo/py/sign/only.json", 'w', encoding='utf-8') as f:
    f.write(json.dumps(dic, ensure_ascii=False, indent=4))