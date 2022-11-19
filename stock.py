import math
from tensorflow import keras
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Tkagg')
import time as t
import numpy as np
import pandas as pd
from datetime import time,date
import pandas_datareader as web
import streamlit as st
from keras.layers import LSTM, Dense, Dropout
from keras.models import Sequential
from sklearn.preprocessing import MinMaxScaler

plt.style.use('fivethirtyeight')
st.title('Stock Trend Prediction')
list_stocks=[ ['AMZN','(AMAZON)'],["CCL","(Carnival Corporation)"],
 ["AMD","(Advanced Micro Devices)"],[ "NVDA","(NVIDIA Corporation )" ],["AAPL","(Apple Inc)"],
 ["TSLA","(Tesla)"],[ "F","(FORD)"],["META","(Meta Platforms)"],
 ["CSCO","(CISCO)"],["GOOG","(GOOGLE)"],["NFLX","(NETFLIX)"],["TWTR","(TWITTER)"]]
user_in=st.selectbox("select from below",list_stocks)
# user_in=st.text_input('Enter Stock Ticker','AAPL')
df=web.DataReader(user_in[0], data_source='yahoo',start='2010-01-01',end='2022-11-19')
# ORIGINAL CLOSING PRICE 

start_time = st.slider(
    "When do you start?",
    value=(date(2010, 1, 1),date(2022, 11, 19)))
t.sleep(2)
#adding sleep so that we could get time to select stock and date
df=web.DataReader(user_in[0], data_source='yahoo',start=start_time[0],end=start_time[1])
st.write('Data from ',start_time[0],'to',start_time[1])
st.write(df.describe())
st.subheader('Closing Price vs Time chart')
fig=plt.figure(figsize=(12,6))
plt.xlabel('Date',fontsize=18)
plt.ylabel('closing price USD($)')
plt.plot(df.Close)
plt.legend()
st.pyplot(fig)