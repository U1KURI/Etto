import streamlit as st
import time

st.title("Streamlit 超入門")

st.write("プログレスバーとUI機能")

'Start!!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range (100):
    latest_iteration.text(f'{i + 1} %')
    bar.progress( i + 1 ) 
    time.sleep(0.05)

'Done!!!'



left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('右カラム｢左カラムでボタンが押されました｣')

expander1 = st.expander('ほげ')
expander1.write('ほげほげ')

expander2 = st.expander('ふげ')
expander2.write('ふげふげ')

# df = pd.DataFrame(
#     np.random.rand(100,2)/[50, 50] + [35.69, 139.70],
#     columns=["lat","lon"]
# )

# st.map(df)

# st.dataframe(df.style.highlight_max(axis=0), width=200, height=500)
# st.table(df.style.highlight_max(axis=0))
