import streamlit as st
#import numpy as np
#import pandas as pd
#from PIL import Image
import time

st.title("streamlit 超入門")
#st.write("DataFrame")


#df = pd.DataFrame({
#    "1列目": [1, 2, 3, 4],
#    "2列目": [10, 20, 30, 40]
#})

#st.write("write")
#st.write(df)

#st.write("dataframe")#幅・高さを指定できるのがポイント
#st.dataframe(df.style.highlight_max(axis=0), width=500 , height= 300) #幅・高さはピクセル単位

#st.write("table")#静的なテーブルになるのがポイント
#st.table(df)


#マジックコマンド マークダウン記法の表示？
#"""
# 章
## 節
### 項

#```python　#ここからpythonのコードを書く場合
#import streamlit as st
#import numpy as np
#import pandas as pd
#```
#"""

#df = pd.DataFrame(
#    np.random.rand(20,3),
#    columns= ['a', 'b', 'c']
#)

#st.line_chart(df)#折れ線グラフ　area_chartや棒グラフbar_chartもある。

#マップへのプロット
#df = pd.DataFrame(
#    np.random.rand(100,2)/[50,50] + [35.69,139.70],
#    columns= ['lat', 'lon']#緯度と経度
#)

#st.map(df)

#st.write("Display image")
#option = st.selectbox(
#    "あなたの好きな数字をおしえてください。",
#    list(range(1,11))
#)

#"あなたが好きな数字は、" ,option, "です。"

#if st.checkbox("show image"):
#   img = Image.open("mark.png")
#    st.image(img,caption="sample",use_column_width=True)

#サイドバーに表示したいときは、st.sidebar.write()等とすればOK
st.write("インタラクティブなウィジェット")

#text = st.text_input("あなたの趣味をおしえてください。")
#"あなたの趣味：" ,text, "です。"

#condition = st.slider("あなたの今の調子は？",0,100,50)
#"コンディション：" ,condition, "です。"

left_column,right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラム")

#エクスパンダーは拡張的なものFAQなど
expander1 = st.expander("問い合わせ1")
expander1.write("問い合わせ1の回答")
expander2 = st.expander("問い合わせ2")
expander2.write("問い合わせ2の回答")
expander3 = st.expander("問い合わせ3")
expander3.write("問い合わせ3の回答")


st.write("プログレスバーの表示")
"start"
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i + 1)
    time.sleep(0.1)

"done"