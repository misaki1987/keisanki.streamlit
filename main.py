import streamlit as st
import pandas as pd
import time

st.title("streamlitで作った計算機")
"""
## 基礎情報
"""
hosp = st.sidebar.selectbox(
    "あなたの入院日数をおしえてください。",
    list(range(0,31))
)
gtth = st.sidebar.selectbox(
    "あなたの通院日数を教えてください。",
    list(range(0,31))
)
grade = st.sidebar.selectbox(
    "認定されている後遺障害等級を指定してください。",
    list(range(0,15))
)
condition = st.sidebar.slider("過失割合は？",0,100,50)

"入院日数：" ,hosp
"通院日数：" ,gtth
"過失割合：" ,condition

"""
## 自賠責基準
"""
sol3 = 0
if grade == 0:
    sol3 = 0
elif grade == 1:
    sol3 = 11500000
elif grade == 2:
    sol3 = 9980000
elif grade == 3:
    sol3 = 8610000
elif grade == 4:
    sol3 = 7370000
elif grade == 5:
    sol3 = 6180000
elif grade == 6:
    sol3 = 5120000
elif grade == 7:
    sol3 = 4190000
elif grade == 8:
    sol3 = 3310000
elif grade == 9:
    sol3 = 2490000
elif grade == 10:
    sol3 = 1900000
elif grade == 11:
    sol3 = 1360000
elif grade == 12:
    sol3 = 940000
elif grade == 13:
    sol3 = 570000
elif grade == 14:
    sol3 = 320000

"入院慰謝料：", hosp * 4300
"通院慰謝料：", gtth * 4300
ex1 = st.expander("慰謝料の計算式")
ex1.write("自賠責基準の場合、慰謝料は１日４３００円です。")
"後遺障害慰謝料", sol3

"""
## 赤本基準（別表Ⅰ）
"""
#入院慰謝料sol1の計算
sol1 = 0
if hosp <= 30:
    sol1 = int(530000 * hosp /30)
elif hosp <= 60:
    sol1 = 530000 + 480000 * (hosp-30)/30
#通院慰謝料sol2の計算
sol2 = 0
if hosp == 0 :
    if gtth <= 30: sol2 = int(280000 * gtth /30)
elif hosp > 0 :
    if hosp + gtth <= 30:
        sol2 = (280000 * (hosp + gtth)/30) - (280000 * hosp /30)
    elif hosp + gtth <= 60:
        sol2 = (280000 + 240000 * ((hosp + gtth)-30)/30) - (280000 * hosp /30)
        
sol3 = 0
if grade == 0:
    sol3 = 0
elif grade == 1:
    sol3 = 28000000
elif grade == 2:
    sol3 = 23700000
elif grade == 3:
    sol3 = 19900000
elif grade == 4:
    sol3 = 16700000
elif grade == 5:
    sol3 = 14000000
elif grade == 6:
    sol3 = 11800000
elif grade == 7:
    sol3 = 10000000
elif grade == 8:
    sol3 = 8300000
elif grade == 9:
    sol3 = 6900000
elif grade == 10:
    sol3 = 5500000
elif grade == 11:
    sol3 = 4200000
elif grade == 12:
    sol3 = 2900000
elif grade == 13:
    sol3 = 1800000
elif grade == 14:
    sol3 = 1100000
    
"入院慰謝料：", int(sol1) 
"通院慰謝料：", int(sol2)
ex1 = st.expander("慰謝料の計算式")
ex1.write("赤本基準の場合、慰謝料は・・・です。")
"後遺障害慰謝料", sol3

"""
## 比較表
"""
df = pd.DataFrame({
    "1列目": [1, 2, 3, 4],
    "2列目": [10, 20, 30, 40]
#})


st.write("作成中につき取扱注意")
