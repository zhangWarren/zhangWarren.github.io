import unittest
import requests
from ddt import ddt,data
from tools.http_request import HttpRequest
from tools.project_path import *
from tools.get_data import GetData
from tools.do_excel import DoExcel
from tools.do_mysql import DoMysql
from tools.my_log import MyLog
from tools.get_token import GetToken


my_loger =MyLog()
test_data = DoExcel().get_data(test_case_path)
print(test_data)
# @ddt
# class TestHttpRequest(unittest.TestCase):
#     def setUp(self):
#         pass
#     @data(*test_data)
#     def test_api(self,item):
#         # my_loger.info('开始执行用例{0}:{1}'.format(item['case_id'],item['title']))
#         # 请求之前完成loan_id的替换
#         # if item['data'].find('${loan_id}')!=-1:
#         #     if getattr(GetData,'loan_id')==None:
#         #         query_sql = 'select max(Id) from loan where MemberID={0}'.format(getattr(GetData,'loan_member_id'))
#         #         loan_id = DoMysql().do_mysql(query_sql)[0][0]
#         #         item['data'] = item['data'].replace('${loan_id}',str(loan_id))
#         #         setattr(GetData,'loan_id',loan_id) # 利用这个反射去存储结果
#         #     else:
#         #         item['data']=item['data'].replace('${loan_id}',str(getattr(GetData,'loan_id')))
#         # my_loger.info((loan_id))
#         # my_loger.info('获取到的请求数据是：{0}'.format(item['data']))
#         my_loger.info('---------开始http接口请求-----------')
#
#
#         print(res.json())
#
#         if res.accessToken:
#             token = res.json()['data']['accessToken']
#             token = "Bearer" + " " + token
#             headers = {
#                 "authorization": token}
#             setattr(GetData, 'headers', headers)
#         try:
#             self.assertEqual(item['expected'],res.json()['code'])
#             TestResult = 'PASS'
#         except AssertionError as e:
#             TestResult = 'Failed'
#             my_loger.info("执行用例出错:{0}".format(e))
#             raise e
#         finally:#不管是对是错，它里面的代码一定要执行
#             DoExcel().write_back(test_case_path,item['sheet_name'],item['case_id']+1,str(res.json()),TestResult)
#             my_loger.error("执行用例出错:{0}".format(res.json()))
#             print("获得的结果是：{0}".format(res.json()))
#
#
#     def tearDown(self):
#         pass

@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        pass
    @data(*test_data)
    def test_api(self,item):
        # my_loger.info('开始执行用例{0}:{1}'.format(item['case_id'],item['title']))
        # 请求之前先登录
        # url = 'http://online.sit.huahuihr.com/up/api/Authorization/AccountLogin'
        # payload = {
        #     "account": '17322342002',
        #     "password": '123456'
        # }
        # res = requests.post(url, json=payload)
        # token = res.json()['data']['accessToken']
        # token = "Bearer" + " " + token
        # headers = {
        #             "authorization": token
        #                     }
        # # setattr(GetData, 'headers', headers)



        #         setattr(GetData,'loan_id',loan_id) # 利用这个反射去存储结果
        #     else:
        #         item['data']=item['data'].replace('${loan_id}',str(getattr(GetData,'loan_id')))
        # my_loger.info((loan_id))
        # my_loger.info('获取到的请求数据是：{0}'.format(item['data']))
        # my_loger.info('---------开始http接口请求-----------')

        # headers =eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI4YzgyN2M3MS02ZTM3LTRkMjgtYWQ0Zi1lYjA2Mzc0MzdlYjYiLCJpYXQiOjE2MTYwNjQwODAsInRva2VuX3ZhbGlkaXR5X2tleSI6IjZjOTBiMGMwLTM0MWItNDNiNi05NzIwLTExNTAyNzk5MmRjYyIsImF1ZCI6WyJodWFodWloci5jb20iLCJodWFodWloci5jb20iXSwiaXNzIjoiaHVhaHVpIiwidXNlcl9pZGVudGlmaWVyIjoiYmYzZDA5M2UtNjg4MS00NTNjLTk0ZGMtNDYwN2VhZmJlOGVkIiwiaWQiOiJiZjNkMDkzZS02ODgxLTQ1M2MtOTRkYy00NjA3ZWFmYmU4ZWQiLCJuYW1lIjoi5byg5Lyf5LicIiwicGhvbmVfbnVtYmVyIjoiMTM1MzA0NzM3MDgiLCJhY2NvdW50IjoiMTM1MzA0NzM3MDgiLCJpZGNhcmRubyI6IjQ0MTYyMTE5ODYwNDE1NTkxMyIsIm5iZiI6MTYxNjA2NDA4MCwiZXhwIjoxNjI0NzA0MDgwfQ.XxTk7E7Co4IncmRFcdWHCl60cn1SjPPy-uLl8Y6BpCE"
        res = HttpRequest().http_request(item['url'], item['http_method'],eval(item['data']),headers=GetToken().token())



        try:
            if item['result_type']== "success":
            # self.assertEqual(item['expected'],res.json()['code'])
                self.assertTrue(res.json()['success'])
            elif item['result_type']== "message":
                self.assertEqual(item['expected'], res.json()['message'])

            TestResult = 'PASS'
        except AssertionError as e:
            TestResult = 'Failed'
            my_loger.info("执行用例出错:{0}".format(e))
            raise e
        finally:
            DoExcel().write_back(test_case_path,item['sheet_name'],item['case_id']+1,str(res.json()),TestResult)
            # my_loger.error("执行用例出错:{0}".format(res.json()))
            print("获得的结果是：{0}".format(res.json()))
