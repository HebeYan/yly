from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from email import encoders
from email.mime.base import MIMEBase


def send_mail(sender, psw, receiver, smtpserver, report_file, port,mail_body):
    '''第四步：发送最新的测试报告内容'''
    # 定义邮件内容
    msg = MIMEMultipart()
    body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    msg['Subject'] = u"UI自动化测试报告"
    msg["from"] = sender
    msg["to"] = psw
    msg.attach(body)
    # 添加附件
    part=MIMEBase('application','octet-stream')
    part.set_payload(open(report_file, "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="WorkBook3.xlsx"')
    msg.attach(part)
    try:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
    except:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver, port)
    # 用户名密码
    smtp.login(sender, psw)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print('test report email has send out !')

