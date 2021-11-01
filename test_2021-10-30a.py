import pandas as pd 
import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
#from fbprophet import Prophet

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

st.line_chart(data.Close)
st.line_chart(data.Volume)

# preparing the data for Facebook-Prophet.
#data = data.reset_index()
#data_pred = data[['Date','Close']]
#data_pred=data_pred.rename(columns={"Date": "ds", "Close": "y"})

# code for facebook prophet prediction
#m = Prophet()
#m.fit(data_pred)
#future = m.make_future_dataframe(periods=period)
#forecast = m.predict(future)

#st.line_chart(forecast.y)
#st.write(forecast)
