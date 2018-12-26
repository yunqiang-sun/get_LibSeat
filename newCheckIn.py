#!/usr/bin/env python
# -*- coding: utf-8 -*-

# UJNLib Host地址:https://seat.ujn.edu.cn:8443

import requests
import datetime
import json
import sys
import urllib3
urllib3.disable_warnings()
reload(sys)
sys.setdefaultencoding('utf-8')

r = requests.get('http://127.0.0.1/checkIn.json')

login_headers = {
    'Host': 'seat.ujn.edu.cn:8443',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Connection': 'keep-alive',
    'Accept': '*/*',
    'User-Agent': 'doSingle/11 CFNetwork/811.5.4 Darwin/16.6.0',
    'Accept-Language': 'zh-cn',
    'token': 'ALO6C40F1I07052859',
    'Accept-Encoding': 'gzip'
}
page_json = json.loads(r.text)
for i in range(page_json['length']):
    s=page_json['data'][i]['studentNum']
    getTokenURL='https://seat.ujn.edu.cn:8443/rest/auth?username='+page_json['data'][i]['studentNum']+'&password='+page_json['data'][i]['password']
    tokenResponse=requests.get(getTokenURL,headers=login_headers,verify=False)
    login_json = json.loads(tokenResponse.text)
    token=login_json['data']['token']
    print(token)
    #checkInURL='https://seat.ujn.edu.cn:8443/rest/v2/checkIn?token='+token
    checkInURL='https://seat.ujn.edu.cn:8443/rest/v2/checkIn'
    headers = {
        'Host': 'seat.ujn.edu.cn:8443',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'User-Agent': 'doSingle/11 CFNetwork/811.5.4 Darwin/16.6.0',
        'Accept-Language': 'zh-cn',
        'token': token,
        'Accept-Encoding': 'gzip'
    }
    page=requests.get(checkInURL,headers=headers,verify=False)
    print s   
    print(page.text)
