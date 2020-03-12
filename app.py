import streamlit as st
from opentrend import lanTrend
import altair as alt


st.title("OpenTrend")

koa = lanTrend.Koa()

table = koa.getTable()
perTable = (table.T / table.sum(1)).T
# perTable.plot()
c = alt.Chart(perTable).mark_line().encode(y="Python")
st.write(c)
# st.table(table)

