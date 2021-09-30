from streamlit.type_util import data_frame_to_bytes
import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# A Simple Stock Price app

Shown are the closing prices and volumes of Google Stocks
""")

ticker = 'GOOGL'

data = yf.Ticker(ticker)

df = data.history(period = '1d', start = '2010-5-31', end = '2021-9-29')

st.line_chart(df.Close)
st.line_chart(df.Volume)