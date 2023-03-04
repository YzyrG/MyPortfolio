import streamlit as st
import pandas  # 用来读data.csv

# 页面宽屏显示+修改page名称+增加page icon
st.set_page_config(layout="wide", page_title="My Python Portfolio | ZYR ", page_icon="🥑")

# web 页面内容分为两列展示
column1, column2 = st.columns(2)

with column1:
    st.image("Images/me.JPG", width=350)

with column2:
    st.header("ZYR")
    content_1 = """
    Hi, I am Yarong Zhang！我是一名编程学习者，目前正在学习python语言&练习一些小项目。
    我于2019年毕业于西南大学商贸学院信息管理与信息系统专业，曾在上海泛微网络科技有限公司担任测试工程师的角色，
    主要负责公司产品e-cology系统公文模块的功能测试任务。但相比测试我更想倾向于做一名编程者，所以正在因此而努力:)
    """
    st.info(content_1)

content_2 = """
    欢迎参观我的个人网站！下面是我做过的一些Python项目, Feel free to contact me. (^-^)\n
    """
st.write(content_2)

# 使用Pandas读取data.csv
data = pandas.read_csv("data.csv", sep=';')
column3,  column4 = st.columns(2)

with column3:
    for index, row in data[:10].iterrows():  # title, description, url, image与相应数据对应起来
        st.subheader(row["title"])
        st.write(row['description'])
        st.image(f"Images/{row['image']}", width=300)
        st.write(f"[source code]({row['url']})")  # 链接名称为source code，实际为row['url']

with column4:
    for index, row in data[10:].iterrows():
        st.subheader(row['title'])
        st.write(row['description'])
        st.image(f"Images/{row['image']}", width=300)
        st.write(f"[source code]({row['url']})")
