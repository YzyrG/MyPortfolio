"""
Send email function
"""
from email.mime.text import MIMEText
from email.utils import formataddr
import smtplib  # SMTP简单邮件传输协议
import ssl
import os


# 构造邮件格式
def create_email(user_email, pure_message):
    msg = MIMEText(pure_message, 'plain', 'utf-8')
    msg['From'] = formataddr(('My Portfolio User', user_email))
    msg['To'] = formataddr(('ZYR', '2456327328@qq.com'))
    msg["Subject"] = f"New email from {user_email}"
    return msg


def send_email(message):
    # 使用163邮箱作为SMTP服务器
    host = "smtp.163.com"
    port = 465

    # 代发人邮箱地址，代发人sender代替user_email发送邮件给接受邮件的receiver
    sender = "15683966878@163.com"
    password = os.getenv("PASSWORD")

    receiver = "2456327328@qq.com"
    # 返回一个新的带有安全默认设置的上下文
    context = ssl.create_default_context()

    # 使用安全加密的SSL协议连接到SMTP服务器
    with smtplib.SMTP_SSL(host, port, context=context, timeout=60) as server:
        # 使用password登录sender的邮箱
        server.login(sender, password)
        # sender发送message给receiver
        server.sendmail(sender, receiver, message)
