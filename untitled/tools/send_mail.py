import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

_user = '584912258@qq.com'
_pwd = 'zhangweidong765'

now = time.strptime('%Y-%m-%d_%H_%M_%S')  # 获取时间戳

class sendEmail:
    def send_email(self,email_to,filepath): # email_to是发件方，filepath是附件地址
        msg = MIMEMultipart()
        msg["Subject"] = now+"测试报告" # 发送邮件的主题
        msg["From"] = _user
        msg["To"] = email_to
        # 这是正文
        part = MIMEText("这是自动化测试结果，请查收！")
        msg.attach(part)

        # 附件部分
        part = MIMEApplication(open(filepath,'rb').read())
        part.add_header('Content-Disposition','attachment',filename=filepath)
        msg.attach(part)
        s = smtplib.SMTP_SSL("smtp.163.com", timeout=30) # 连接SMTP邮件服务器
        s.login(_user,_pwd) # 登陆服务器
        s.sendmail(_user,email_to,msg.as_string()) # 发送邮件
        s.close()

if __name__ == '__main__':
    sendEmail().send_email("584912258@qq.com",r'E:')