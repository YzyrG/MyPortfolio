"""
Contact me page
"""

import streamlit as st
from send_email import create_email, send_email

# 页面宽屏显示+修改page名称+增加page icon
st.set_page_config(layout="wide", page_title="My Python Portfolio | ZYR ", page_icon="🥑")

st.header("Contact Me ٩(ˊᗜˋ*)و")

with st.form(key="email_contact"):  # clear_on_submit=True 按下Submit后重置form为默认值
    user_email = st.text_input('Your email address', key='email')
    pure_message = st.text_area("Your message", key="message")
    receiver_email = "15683966878@163.com"
    message = create_email(user_email, pure_message)
    button = st.form_submit_button("Submit")
    # print(button)
    if button:  # 点击Submit后button值为True
        # print(button)
        try:
            message = f"{message}"
            send_email(message)
            st.info("Your email was sent successfully!")
        except TimeoutError:
            st.info(":( Sorry, Seems like you have a bad internet connection. Please try again later. ")

