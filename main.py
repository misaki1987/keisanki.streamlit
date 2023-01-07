import streamlit as st
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
condition = st.sidebar.slider("過失割合は？",0,100,50)

"入院日数：" ,hosp
"通院日数：" ,gtth
"過失割合：" ,condition

"""
## 自賠責基準（別表Ⅰ）
"""
"入院慰謝料：", hosp * 4300
"通院慰謝料：", gtth * 4300
ex1 = st.expander("慰謝料の計算式")
ex1.write("自賠責基準の場合、慰謝料は１日４３００円です。")

"""
## 赤本基準
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
    
"入院慰謝料：", int(sol1) 
"通院慰謝料：", int(sol2)
ex1 = st.expander("慰謝料の計算式")
ex1.write("赤本基準の場合、慰謝料は・・・です。")

st.write("作成中につき取扱注意")
