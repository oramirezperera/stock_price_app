import yfinance_ez as yf
import streamlit as st
import pandas as pd

st.title("""
# Stock Price app

""")
st.write("""
This app shows the closing price and the volume of a given ticker symbol
""")

ticker_symbol = 'TSLA'

# This downloads some of the data from the ticker symbol

ticker_data = yf.Ticker(ticker_symbol)

# This gets info about the ticker
st.write("""
## Info about the selected stock
""")
ticker_info = st.write(ticker_data.info)

# Historical data from the ticker 
# period can be: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
# default is 1mo
ticker_df = ticker_data.get_history(period=yf.TimePeriods.Quarter)
st.write("""
## Here are the closing value of the stock
""")
st.line_chart(ticker_df.Close)
st.write("""
## Volume of the stock
""")
st.line_chart(ticker_df.Volume)