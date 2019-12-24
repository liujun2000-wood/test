#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/12/10 17:32
#@Author: liujun
#@File  : confighttp.py
import requests
import json
class RunMain():

    def send_post(self,url,data):
        result = requests.post(url=url,data=data).json()
        # 因为这里要封装post方法，所以这里的url和data值不能写死
        res = json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)
        return res
    def send_get(self,url,data):
        result = requests.get(url,params=data).json()
        # result = requests.get(url=url,data=data).json()
        print(url,data)
        res = json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)
        return res
    def run_main(self,method,url=None,data=None):
        result = None
        if method == 'post':
            result = self.send_post(url,data)
        elif method == 'get':
            result = self.send_get(url,data)
        else:
            print("method类型不支持")
        return result
if __name__ == '__main__':
    result1 = RunMain().run_main('post','http://127.0.0.1:8888/login',{'name': 'xiaoming','pwd':'111'})
    result2 = RunMain().run_main('get','http://127.0.0.1:8888/login', 'name=xiaoming&pwd=111')
    print(result1)
    print(result2)
