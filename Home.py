"""
 My Portfolio home page
"""
import urllib3
import streamlit as st
import pandas  # 用来读data.csv
import requests

# ----------------------------------------首页展示NASA图片-----------------------------------------------#
# 通过api拿到图片json文件并读取
api_key = "tnsxcGgQyfXgTMwhPTlBgSDBt0LNKyNOmzsr6FZd"
url = "https://api.nasa.gov/planetary/apod?" \
      f"api_key={api_key}"
headers = {'Connection': 'close'}

# 不显示InsecureRequestWarning警告
urllib3.disable_warnings()

# 请求页面
request = requests.get(url, headers=headers, verify=False)
content_1 = request.json()
print(content_1)
# 读取json
date = content_1["date"]
title = content_1['title']
img_copyright = content_1['copyright']
img_url = content_1["url"]
explanation = content_1["explanation"]

# 请求图片
img = requests.get(img_url)
content_2 = img.content

# 将图片存入文件夹images
img_filepath = f"images/{date}.jpg"
with open(img_filepath, 'wb') as file:
    file.write(content_2)


# ------------------------------------------------UI设计--------------------------------------------------------#
# 页面宽屏显示+修改page名称+增加page icon
st.set_page_config(layout="wide", page_title="My Python Portfolio | ZYR ", page_icon="🌘")

# 显示NASA图片
st.image(img_filepath)

# 图片来源说明
st.text(f"{title} by {img_copyright} from NASA Astronomy Picture of the Day.")

# 作品展示
content_2 = """
    欢迎来到这里，祝您冲浪愉快！o(*￣︶￣*)o\n
    """
st.header(content_2)

# 显示自我介绍
content_1 = """
嗨！我叫ZYR, 是一名编程学习者，目前正在学习python语言&练习一些小项目。
我于2019年毕业于西南大学商贸学院信息管理与信息系统专业，
曾在上海泛微网络科技有限公司担任测试工程师的角色，
主要负责公司产品e-cology系统公文模块的功能测试任务。
但相比测试我更想倾向于做一名可以自己开发的编程者，所以正在因此而努力:)\n\n
"""
st.info(content_1)

# 使用Pandas读取data.csv
data = pandas.read_csv("data.csv", sep=';')
column3, column4 = st.columns(2)

with column3:
    #  iterrows()使得各行数据与第一行相应类别对应起来
    for index, row in data[:4].iterrows():
        st.subheader(row["title"])
        st.write(row['description'])
        st.image(f"Images/{row['image']}", width=300)
        # 链接名称为source code，实际为row['url']
        st.write(f"[source code]({row['url']})")

with column4:
    for index, row in data[4:].iterrows():
        st.subheader(row['title'])
        st.write(row['description'])
        st.image(f"Images/{row['image']}", width=300)
        st.write(f"[source code]({row['url']})")
