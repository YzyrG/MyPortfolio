"""
Send email function
"""

import smtplib  # SMTP简单邮件传输协议
import ssl


def send_email(message):
    host = "smtp.gmail.com"  # 使用gmail作为SMTP服务器
    port = 465

    # 发件人邮箱地址
    sender = "zyr724725@gmail.com"
    password = "mvfuxlgpjbowoqbt"

    # 收件人与发件人邮箱地址可以相同也可以不同，只要都是属于自己的gmail账号就可以
    receiver = "zyr724725@gmail.com"
    context = ssl.create_default_context()

    # 使用安全加密的SSL协议连接到SMTP服务器
    with smtplib.SMTP_SSL(host, port, context=context, timeout=60) as server:
        server.login(sender, password)  # 使用password登录sender的邮箱
        server.sendmail(sender, receiver, message)  # sender发送message给receiver
