import streamlit as st
#import numpy as np
#import pandas as pd
#from PIL import Image
import time

st.title("streamlitで作った計算機")
"""
## 基礎情報
"""
hosp = st.sidebar.selectbox(
    "あなたの入院日数をおしえてください。",
    list(range(1,31))
)
gtth = st.sidebar.selectbox(
    "あなたの通院日数を教えてください。"
    list(range(1,31))
)
condition = st.sidebar.slider("過失割合は？",0,100,50)

"入院日数：" ,hosp
"通院日数：" ,gtth
"過失割合：" ,condition

"""
## 自賠責基準（別表Ⅰ）
"""
"入院慰謝料：", 530000 * hosp / 30 
"通院慰謝料：", gtth
ex1 = st.expander("計算式１")
ex1.write("自賠責基準の場合、慰謝料は１日４３００円です。")

"""
## 赤本基準
"""
"入院慰謝料：", hosp * 4300
"通院慰謝料：", gtth * 4300
ex1 = st.expander("計算式１")
ex1.write("自賠責基準の場合、慰謝料は１日４３００円です。")

st.write("作成中")
