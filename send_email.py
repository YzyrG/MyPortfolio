"""
Send email function
"""
from email.mime.text import MIMEText
from email.utils import formataddr
import smtplib  # SMTP简单邮件传输协议
import ssl


def create_email(user_email, pure_message):  # 构造邮件格式
    msg = MIMEText(pure_message, 'plain', 'utf-8')
    msg['From'] = formataddr(('My protfolio User', user_email))
    msg['To'] = formataddr(('ZYR', '15683966878@163.com'))
    msg["Subject"] = f"New email from {user_email}"
    return msg


def send_email(message):
    host = "smtp.163.com"  # 使用163邮箱作为SMTP服务器
    port = 465

    # 代发人邮箱地址，代发人sender代替user_email发送邮件给接受邮件的receiver
    sender = "15683966878@163.com"
    password = "ZSDIBOHXCOCYCYOJ"

    receiver = "2456327328@qq.com"
    context = ssl.create_default_context()  # 返回一个新的带有安全默认设置的上下文

    # 使用安全加密的SSL协议连接到SMTP服务器
    with smtplib.SMTP_SSL(host, port, context=context, timeout=60) as server:
        server.login(sender, password)  # 使用password登录sender的邮箱
        server.sendmail(sender, receiver, message)  # sender发送message给receiver
