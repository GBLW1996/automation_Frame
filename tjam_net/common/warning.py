# _*_ coding:utf-8 _*_
import requests
import json


# 百助测试部门token
# https://oapi.dingtalk.com/robot/send?access_token=273e79e103fd6d5705fcb6a6282df47640efdd047457dfc56a00ba620cd2c1d9
# 测试用
# https://oapi.dingtalk.com/robot/send?access_token=80755986d0bc927e5e4b8b6c26ccf3d3e2d6782d7672aef800127bf01699a184

def message(a):
    url = 'https://oapi.dingtalk.com/robot/send?access_token=' \
          '273e79e103fd6d5705fcb6a6282df47640efdd047457dfc56a00ba620cd2c1d9'
    pagrem = {
        "msgtype": "text",
        "text": {
            "content": "站点自动化测试：%s " % (a)

        },
        "at": {
            "atMobiles": [
                "18365049450",
                ""  # 需要填写自己的手机号，钉钉通过手机号@对应人
            ],
            "isAtAll": False  # 是否@所有人，默认否
        }
    }
    headers = {
        'Content-Type': 'application/json; charset=utf-8'
    }
    requests.post(url, data=json.dumps(pagrem), headers=headers)


if __name__ == "__main__":
    message('自动化测试')
