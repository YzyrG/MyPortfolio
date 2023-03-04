import streamlit as st

# 修改page名称+增加page icon
st.set_page_config(page_title="My Python Portfolio | ZYR ", page_icon="🥑")

# web 页面内容分为两列展示
column1, column2 = st.columns(2)

with column1:
    st.image("Images/me.png", width=200)

with column2:
    st.title("Yarong Zhang")
    content = "欢迎参观我的个人网站！在这里你可以浏览我做过的一些Python项目，参观愉快:)"
    st.info(content)

