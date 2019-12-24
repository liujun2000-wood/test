#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/12/12 23:23
#@Author: liujun
#@File  : test01case.py

import json
import unittest
#因为pycharm工程当前目录在上一层。所以需要从目录开始引用。
from omegafaceTest.common.confighttp import RunMain
import omegafaceTest.geturlParams
# import paramunittest
import omegafaceTest.readExcel
import urllib.parse

url = omegafaceTest.geturlParams.geturlParams().get_Url()# 调用我们的geturlParams获取我们拼接的URL
login_xls = omegafaceTest.readExcel.readExcel().get_xls('userCase1.xlsx', 'userCase')
class testUserLogin(unittest.TestCase):
    def setParameters(self,case_name,path,query,method):
        '''
        set params
        :param case_name:
        :param path:
        :param query:
        :param method:
        :return:
        '''
        self.case_name = str(case_name)
        self.path = str(path)
        self.query = str(query)
        self.method = str(method)
    def description(self):
        """
        test report description
        :return:
        """
        print(self.case_name+"测试开始前准备")
    def test01case(self):
        result1 = RunMain.run_main('get',url,login_xls[1][2])
        print(result1)
        self.checkResult()

    def tearDowm(self):
        print('测试结束,输出log完结\n\n')
    def checkResult(self):
        """
        check test result
        :return:
        """
        url1 = "http://www.xxx.com/login?"
        new_url = url1 +self.query
        # 将一个完整的URL中的name=&pwd=转换为{'name':'xxx','pwd':'bbb'}
        data1 = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))
        info = RunMain().run_main(self.method, url, data1)  # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        ss = json.loads(info)
        if self.case_name == 'login':
            self.assertEqual(ss['code'],200)
        if self.case_name == 'login_error':
            self.assertEqual(ss['code'],-1)
        if self.case_name == 'login_null':
            self.assertEqual(ss['code'],10001)
if __name__ == '__main__':
    testUserLogin