"""
Contact me page
"""

import streamlit as st
from send_email import create_email, send_email

# 页面宽屏显示+修改page名称+增加page icon
st.set_page_config(layout="wide", page_title="My Python Portfolio | ZYR ", page_icon="🥑")

st.header("Contact Me ٩(ˊᗜˋ*)و")

with st.form(key="email_contact"):
    user_email = st.text_input('Your email address', key='email')
    pure_message = st.text_area("Your message", key="message")
    receiver_email = "15683966878@163.com"
    # 返回的message是MIMEText类型
    message = create_email(user_email, pure_message)
    # print(type(message))
    button = st.form_submit_button("Submit")

    # 点击Submit后button值为True
    if button:
        try:
            # 将message转换为string类型数据
            message = str(message)
            send_email(message)
            st.info("Your email was sent successfully!")
        except TimeoutError:
            st.info(":( Sorry, Seems like you have a bad internet connection. Please try again later. ")

