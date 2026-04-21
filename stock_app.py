"""
Stock Market Analyzer Dashboard

Libraries:
- yfinance → data fetching
- pandas → data analysis
- plotly → visualization
- streamlit → UI
"""

import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from ta.trend import SMAIndicator, EMAIndicator
from ta.momentum import RSIIndicator
from ta.volume import VolumePriceTrendIndicator
import streamlit as st

# -------------------------------
# UI CONFIG
# -------------------------------
st.set_page_config(page_title="Stock Analyzer", layout="wide")

st.title("🧠 Stock Market Analyzer Dashboard")
st.sidebar.header("Configuration")

# -------------------------------
# USER INPUT
# -------------------------------
ticker = st.sidebar.text_input("Stock Ticker", value="AAPL")
period = st.sidebar.selectbox("Period", ["1mo", "3mo", "6mo", "1y", "2y", "5y", "max"])
interval = st.sidebar.selectbox("Interval", ["1d", "5d", "1wk", "1mo", "3mo"])

# -------------------------------
# DATA LOADING
# -------------------------------
@st.cache_data(ttl=3600)
def load_data(ticker, period, interval):
    stock = yf.Ticker(ticker)
    df = stock.history(period=period, interval=interval)
    return df

df = load_data(ticker, period, interval)

# -------------------------------
# MAIN LOGIC
# -------------------------------
if df.empty:
    st.error("No data found. Check ticker symbol.")
else:
    # Indicators
    df['SMA_20'] = SMAIndicator(df['Close'], window=20).sma_indicator()
    df['SMA_50'] = SMAIndicator(df['Close'], window=50).sma_indicator()
    df['EMA_12'] = EMAIndicator(df['Close'], window=12).ema_indicator()
    df['RSI'] = RSIIndicator(df['Close']).rsi()
    df['VPT'] = VolumePriceTrendIndicator(df['Close'], df['Volume']).volume_price_trend()

    # -------------------------------
    # METRICS
    # -------------------------------
    current_price = df['Close'].iloc[-1]
    start_price = df['Close'].iloc[0]
    change = current_price - start_price
    latest_rsi = df['RSI'].iloc[-1]

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Current Price", f"${current_price:.2f}")

    with col2:
        st.metric("Change", f"${change:.2f}",
                  delta=f"{(change/start_price*100):.2f}%")

    with col3:
        st.metric("Volume", f"{df['Volume'].iloc[-1]:,.0f}")

    with col4:
        st.metric("RSI", f"{latest_rsi:.2f}")

    # -------------------------------
    # CHARTS
    # -------------------------------
    fig = make_subplots(
        rows=3, cols=1,
        shared_xaxes=True,
        vertical_spacing=0.05,
        subplot_titles=('Price & Moving Averages', 'Volume', 'RSI'),
        row_width=[0.2, 0.3, 0.5]
    )

    # Candlestick
    fig.add_trace(go.Candlestick(
        x=df.index,
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close'],
        name='Price'
    ), row=1, col=1)

    # Moving averages
    fig.add_trace(go.Scatter(x=df.index, y=df['SMA_20'], name='SMA 20'), row=1, col=1)
    fig.add_trace(go.Scatter(x=df.index, y=df['SMA_50'], name='SMA 50'), row=1, col=1)

    # Volume
    fig.add_trace(go.Bar(
        x=df.index,
        y=df['Volume'],
        name='Volume'
    ), row=2, col=1)

    # RSI
    fig.add_trace(go.Scatter(x=df.index, y=df['RSI'], name='RSI'), row=3, col=1)
    fig.add_hline(y=70, line_dash="dash", row=3, col=1)
    fig.add_hline(y=30, line_dash="dash", row=3, col=1)

    fig.update_layout(xaxis_rangeslider_visible=False)

    st.plotly_chart(fig, use_container_width=True)

    # -------------------------------
    # INSIGHTS
    # -------------------------------
    st.header("📈 Quick Insights")

    # RSI signal
    if latest_rsi > 70:
        signal = "Overbought (Sell Signal)"
    elif latest_rsi < 30:
        signal = "Oversold (Buy Signal)"
    else:
        signal = "Neutral"

    st.success(f"RSI Signal: {signal}")

    # Trend
    if df['SMA_20'].iloc[-1] > df['SMA_50'].iloc[-1]:
        trend = "Bullish (Uptrend)"
    else:
        trend = "Bearish (Downtrend)"

    st.info(f"Moving Average Trend: {trend}")

    # Volatility
    volatility = df['Close'].pct_change().std() * np.sqrt(252) * 100
    st.metric("Annualized Volatility", f"{volatility:.2f}%")

    # -------------------------------
    # DOWNLOAD
    # -------------------------------
    csv = df.to_csv().encode('utf-8')
    st.download_button("Download Data CSV", csv,
                       f"{ticker}_analysis.csv", "text/csv")

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("---")
st.caption("Built with Python | yfinance | plotly | Streamlit 🚀")