import smtplib
from email.mime.multipart import MIMEMultipart#处理多种形态的邮件主体我们需要 MIMEMultipart 类
from  email.mime.application import MIMEApplication#发送邮件的各个类型
from email.mime.text import MIMEText #发送字符串的邮件
import datetime

def Mail_send():
    #设置服务器信息
    fromaddr="xx"
    password="xxx"
    toaddrs=["xxxx"]



    #设置发送内容
    oneday = datetime.timedelta(days=1)
    today = datetime.date.today()
    yesterday=today-oneday
    content="报告记录时间段：%s 10:30 -- %s 10:30""\r\n""总结：设备链路无异常"%(yesterday,today)
    textapart=MIMEText(content)

    #f设置发送附件
    ytonetwork_list ="/usr/local/python_on/Daily_automation_linux/Daily_word/网络运营日报.doc"
    listapart=MIMEApplication(open(ytonetwork_list,"rb").read())
    listapart.add_header('Content-Disposition', 'attachment',filename="网络运营日报%s.doc"%today)

    #设置发送
    m=MIMEMultipart()
    m.attach(textapart)
    m.attach(listapart)
    m["Subject"]="网络运营日报%s.doc"%today
    m["From"]="ytonetworks机器人"
    m["To"]=toaddrs[0]
    # m["Cc"]=cc

    # m["Content-Type"] = 'application/octet-stream'

    try:
        server =smtplib.SMTP("xxxxx")
        server.login(fromaddr,password)
        server.sendmail(fromaddr,toaddrs,m.as_string())
        print("success")
        server.quit()
    except smtplib.SMTPException as w:
        print("卧槽，bug",w)
if __name__ == '__main__':
    Mail_send()
