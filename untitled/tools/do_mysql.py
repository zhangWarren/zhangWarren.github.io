import mysql.connector
from tools import project_path
from tools.read_config import ReadConfig

class DoMysql:
    def do_mysql(self,query_sql,state='all'): #  query 是查询语句
        db_config =eval( ReadConfig().get_config(project_path.case_config_path,'DB','db_config')) #利用配置文件读取连接数据库的用户名，密码等
        # 创建一个数据库连接
        cnn = mysql.connector.connect(**db_config)

        # 游标cursor
        cursor = cnn.cursor()
        # 执行语句
        cursor.execute(query_sql)
        # 获取结果打印结果
        if state==1:
            res = cursor.fetchone() # 元祖 针对一条数据
        else:
            res = cursor.fetchall() # 列表 针对多行数据
        print(res)
        print(int(res[0])+1)
        # 关闭游标
        cursor.close()
        # 关闭连接
        cnn.close()
        return res

if __name__ == '__main__':
    query_sq = 'select * from areas where id=10001'
    res = DoMysql().do_mysql(query_sq,1)
    print(res)  #获得的是列表嵌套元祖的数据
    print(res[0][0])