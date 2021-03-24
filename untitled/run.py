import unittest
from HTMLTestRunner import HTMLTestRunner
from tools.project_path import *
from tools.test_http_request import TestHttpRequest


suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))

# with open(test_report_path,'wb') as file:
#     runner = HTMLTestRunner(stream=file,title = "这个是单元测试报告1115",description = "这个是单元测试报告1115")
#     runner.run(suite)

runner=unittest.TextTestRunner()
runner.run(suite)