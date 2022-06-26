from matplotlib import ticker
import yfinance as yf
import streamlit as st
import pandas as pd


st.write("""
# Simple stock price app (**by sarit**)
""")


tickersymbol = "GOOGL"
tickerData = yf.Ticker(tickersymbol)
tickerDf = tickerData.history(period='1d',start='2007-5-31',end='2022-6-24')

st.line_chart(tickerDf.Close)
# st.line_chart(tickerDf.Volume)
