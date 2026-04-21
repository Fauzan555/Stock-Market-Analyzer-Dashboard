# 🧠 Stock Market Analyzer Dashboard

An interactive **Streamlit-based Stock Market Analyzer** that fetches real-time stock data, performs technical analysis, and provides actionable insights using financial indicators.

---

## 📌 Project Overview

This project is designed to demonstrate **end-to-end data analysis skills** including:
- Data collection from APIs
- Data processing and feature engineering
- Technical indicator computation
- Interactive data visualization
- Insight generation


---

## ⚙️ Tech Stack

- **Python**
- **Streamlit** → Web UI
- **yfinance** → Stock data API
- **pandas** → Data manipulation
- **plotly** → Interactive visualization
- **ta (Technical Analysis Library)** → Indicators
- **NumPy** → Numerical computation

---

## 🔥 Features

### 📊 Data Fetching
- Fetches real-time historical stock data using `yfinance`
- Supports multiple time periods and intervals

### 📈 Technical Indicators
- Simple Moving Average (SMA 20, SMA 50)
- Exponential Moving Average (EMA 12)
- Relative Strength Index (RSI)
- Volume Price Trend (VPT)

### 📉 Interactive Visualization
- Candlestick chart
- Moving averages overlay
- Volume chart
- RSI indicator with thresholds

### 📌 Key Metrics
- Current Price
- Price Change (absolute & %)
- Volume
- RSI value (Relative Strength Index)

### 🧠 Insights Engine
- RSI-based signals:
  - Overbought (Sell)
  - Oversold (Buy)
  - Neutral
- Trend detection:
  - Bullish / Bearish using SMA crossover
- Volatility calculation

### 📥 Export Feature
- Download analyzed dataset as CSV

---

## 🏗️ Project Workflow

### Step 1: Data Collection
- Used `yfinance` API to fetch stock data dynamically based on user input

### Step 2: Data Processing
- Cleaned and structured time-series data using `pandas`
- Handled missing values and ensured consistency

### Step 3: Feature Engineering
- Computed technical indicators:
  - SMA (Simple Moving Average), EMA (Exponential Moving Average)
  - RSI (Relative Strength Index)
  - VPT (Volume Price Trend)

### Step 4: Visualization
- Built interactive charts using `plotly`
- Combined multiple subplots for better analysis

### Step 5: UI Development
- Designed an interactive dashboard using `streamlit`
- Added sidebar inputs for user control

### Step 6: Insight Generation
- Implemented logic-based signals:
  - RSI thresholds (Relative Strength Index)
  - Moving average crossover

---

## ▶️ How to Run the Project

### Clone the repository
```bash
git clone https://github.com/your-username/stock-market-analyzer.git
cd stock-market-analyzer
