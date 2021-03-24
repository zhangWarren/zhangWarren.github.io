import os
'''专门用来读取路径的值'''

project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]  # 顶级目录


# 测试用例路径
test_case_path = os.path.join(project_path,'test_data','test_data.xlsx')

# 测试报告路径
test_report_path = os.path.join(project_path,'test_result','html_report','test_report.html')

# 配置文件路径
case_config_path = os.path.join(project_path,'conf','case.config')
print(test_case_path)