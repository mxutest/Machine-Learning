import streamlit as st
import yfinance as yf 
import pandas as pd 

st.write("""
## Stock Price Prediction
by Group1 \n
shows ***stock*** closing and volue of **price**
""")


st.title('Stock Forecast App')
stocklist = ('AAPL','MSCT')
option = st.selectbox('Select dataset for prediction',stocklist)
year = st.slider('Year of prediction:',1,4)
period = year * 365

tickerSymbol='AAPL'
data_load_state = st.text('Loading data...')
tickerData=yf.Ticker(tickerSymbol)
data=tickerData.history(period='1d',start="2010-01-01")
data_load_state.text('Loading data... done!')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

# preparing the data for Facebook-Prophet.
data = data.reset_index()
data_pred = data[['Date','Close']]
data_pred=data_pred.rename(columns={"Date": "ds", "Close": "y"})
