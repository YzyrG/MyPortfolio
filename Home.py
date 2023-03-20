"""
 My Portfolio home page
"""
import urllib3
import streamlit as st
import pandas  # 用来读data.csv
import requests
from urllib3.exceptions import InsecureRequestWarning

# ----------------------------------------首页展示NASA图片-----------------------------------------------#
# 通过api拿到图片json文件并读取
api_key = "nPfpfFzVNZLZMnyIgFI4bMrsGBCbUJcsEFeCEBXU"
url = "https://api.nasa.gov/planetary/apod?" \
      f"api_key={api_key}"
headers = {'Connection': 'close'}

# 不显示InsecureRequestWarning警告
urllib3.disable_warnings(InsecureRequestWarning)

# 请求页面
request = requests.get(url, headers=headers, verify=False)
content_1 = request.json()
# print(content_1)
# 读取json

# 判断是图片还是视频
media_type = content_1["media_type"]

img_filepath = ""
date = content_1["date"]
title = content_1['title']
img_url = content_1["url"]
img_copyright = content_1['copyright']
explanation = content_1["explanation"]

# 是图片将图片保存至images文件夹
if media_type == "image":
    # 请求图片
    img = requests.get(img_url)
    content_2 = img.content

    # 将图片存入文件夹images
    img_filepath = f"images/{date}.jpg"
    with open(img_filepath, 'wb') as file:
        file.write(content_2)

# 不是图片暂时显示2023-03-08.jpg
else:
    img_filepath = "images/2023-03-08.jpg"

# print(img_filepath)
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
嗨！我叫ZYR, 是一名编程学习者，目前正在学习Python&练习一些小项目。
如果你也对计算机科学感兴趣的话，欢迎一起学习交流:)\n\n
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
        st.image(f"images/{row['image']}", width=300)
        # 链接名称为source code，实际为row['url']
        st.write(f"[相关链接]({row['url']})")

with column4:
    for index, row in data[4:].iterrows():
        st.subheader(row['title'])
        st.write(row['description'])
        st.image(f"images/{row['image']}", width=300)
        st.write(f"[相关链接]({row['url']})")
