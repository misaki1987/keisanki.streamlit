import streamlit as st
#import numpy as np
#import pandas as pd
#from PIL import Image
import time

st.title("streamlitで作った計算機")
"""
## 自賠責基準
## 赤本基準
"""

option = st.selectbox(
    "あなたの好きな数字をおしえてください。",
    list(range(1,11))
)

"あなたが好きな数字は、" ,option, "です。"

condition = st.slider("過失割合は？",0,100,50)
"過失割合：" ,condition

#エクスパンダーは拡張的なものFAQなど
expander1 = st.expander("計算式１")
expander1.write("計算式の内容")
expander2 = st.expander("計算式2")
expander2.write("計算式の内容")
expander3 = st.expander("計算式3")
expander3.write("計算式３")

作成中！
