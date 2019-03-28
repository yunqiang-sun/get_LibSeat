#!/usr/bin/env python
# -*- coding: utf-8 -*-

# UJNLib Host地址:https://seat.ujn.edu.cn:8443

import requests
import datetime
import json
import sys
import urllib3
urllib3.disable_warnings()

r = requests.get('http://127.0.0.1/newinfo.json')

page_json = json.loads(r.text)
login_headers = {
    'Host': 'seat.ujn.edu.cn:8443',
    'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
    'Connection': 'keep-alive',
    'Accept': '*/*',
    'User-Agent': 'doSingle/11 CFNetwork/811.5.4 Darwin/16.6.0',
    'Accept-Language': 'zh-cn',
    'token': 'Q6NTRKQ4DV07050600',
    'Accept-Encoding': 'gzip',
    'X-Forwarded-For': '10.167.159.118'
}

for i in range(page_json['length']):
    try:
        getTokenURL='https://seat.ujn.edu.cn:8443/rest/auth?username='+page_json['data'][i]['studentNum']+'&password='+page_json['data'][i]['password']
        tokenResponse=requests.get(getTokenURL,headers=login_headers,verify=False)
        login_json = json.loads(tokenResponse.text)
        token=login_json['data']['token']

        date = datetime.date.today()
        date += datetime.timedelta(days=1)
        strdate = date.strftime('%Y-%m-%d')
        headers = {
            'Host': 'seat.ujn.edu.cn:8443',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Connection': 'keep-alive',
            'Accept': '*/*',
            'token': login_json['data']['token'],
            'User-Agent': 'doSingle/11 CFNetwork/811.5.4 Darwin/16.6.0',
            'Accept-Language': 'zh-cn',
            'X-Forwarded-For': '10.167.159.118'
        }
        postdata={
            't':1,
            'startTime':page_json['data'][i]['startTime'],
            'endTime':page_json['data'][i]['endTime'],
            'date':strdate,
            'seat':page_json['data'][i]['seatId'],
            't2':2
        }
        mainURL='https://seat.ujn.edu.cn:8443/rest/v2/freeBook'
        s=requests.post(mainURL,data=postdata,headers=headers,verify=False)
        print(s.text)
    except:
        continue
