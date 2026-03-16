import streamlit as st
import pandas as pd
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA

# --- 1. STRATEGY DEFINITION ---
class SmaCross(Strategy):
    n1 = 10
    n2 = 20

    def init(self):
        self.sma1 = self.I(SMA, self.data.Close, self.n1)
        self.sma2 = self.I(SMA, self.data.Close, self.n2)

    def next(self):
        if crossover(self.sma1, self.sma2):
            self.buy()
        elif crossover(self.sma2, self.sma1):
            self.position.close()

# --- 2. BACKTEST EXECUTION FUNCTION ---
def run_backtest(data):
    bt = Backtest(data, SmaCross, cash=10000, commission=.002)
    stats = bt.run()
    return stats, bt

# --- 3. STREAMLIT UI ---
st.set_page_config(page_title="CryptoStrat Pro", layout="wide")

st.sidebar.title("Settings")
tier = st.sidebar.radio("Account Tier", ["Free", "Premium (Ad-Free)"])

# Mock Ad Layer
if tier == "Free":
    st.sidebar.markdown("---")
    st.sidebar.info("📌 **AD: Trade BTC with 0% fees!**")

st.title("🚀 Crypto Portfolio Backtester")

# Placeholder Data (In a real app, you'd fetch this from Binance)
# For now, we create a tiny dummy dataframe so the app doesn't crash on load
data = pd.DataFrame({
    'Open': [100, 102, 104, 103, 105] * 20,
    'High': [101, 103, 105, 104, 106] * 20,
    'Low': [99, 101, 103, 102, 104] * 20,
    'Close': [100, 102, 104, 103, 105] * 20,
    'Volume': [1000] * 100
}, index=pd.date_range('2024-01-01', periods=100))

if st.button("Run Strategy"):
    stats, bt = run_backtest(data)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Final Equity", f"${stats['Equity Final [$]']:,.2f}")
    col2.metric("Return", f"{stats['Return [%]']:.2f}%")
    col3.metric("Max Drawdown", f"{stats['Max. Drawdown [%]']:.2f}%")
    
    st.text(stats) # Displays the full stats table
