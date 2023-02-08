import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt

# データ分析関係
df = pd.read_csv('../testdata.csv', index_col='月')
st.dataframe(df)
st.table(df)
st.line_chart(df)
st.bar_chart(df['2021年'])

# matplotlib
fig, ax = plt.subplots()
ax.plot(df.index, df['2021年'])
ax.set_title('matplotlib graph')
st.pyplot(fig)
