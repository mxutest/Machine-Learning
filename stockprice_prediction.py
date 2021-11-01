import streamlit as st
from datetime import date

import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go

st.markdown(
	"""
	<style>
	.main {
     	background-color: #F5F5F5;
	}
	</style>
	""",
	unsafe_allow_html=True
)

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title('Stock Price Prediction - Group1')

stocks = ('GOOG', 'AAPL', 'MSFT', 'GME','Others')
selected_stock = st.selectbox('Select stock symbol for prediction or select Others', stocks)

if selected_stock == 'Others':
	selected_stock = st.text_input('Please input stock code','')

n_years = st.slider('Years of prediction:', 1, 4)
period = n_years * 365

@st.cache
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data
    
data_load_state = st.text('Loading data...')
data = load_data(selected_stock)
data_load_state.text('Loading data... done!')

st.subheader('Raw data')
st.write(data.tail())

# Plot raw data
def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open "+selected_stock))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close "+selected_stock))
    fig.layout.update(title_text='Stock History Price for '+selected_stock, xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)
    
plot_raw_data()

# Predict forecast with Prophet.
df_train = data[['Date','Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

# Show and plot forecast
st.subheader('Forecast data of '+selected_stock)
st.write(forecast.tail())
    
st.write('Forecasting closing of stock value for '+selected_stock+' for a period of: '+str(n_years)+'year')
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write('Forecast components of stock value for '+selected_stock+' for a period of: '+str(n_years)+'year')
fig2 = m.plot_components(forecast)
st.write(fig2)
