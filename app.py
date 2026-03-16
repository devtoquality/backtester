import streamlit as st
import pandas as pd
from backtester import run_backtest

# --- UI CONFIG ---
st.set_page_config(page_title="CryptoStrat Pro", layout="wide")

# --- MOCK AD REVENUE LAYER ---
def show_ads(user_tier):
    if user_tier == "Free":
        st.sidebar.markdown("---")
        st.sidebar.info("📌 **AD: Trade with 0% fees on AquaExchange!** [Link]")
        st.markdown("<div style='background-color:#f0f2f6; padding:10px; text-align:center;'>Sponsored: Get $50 in BTC when you sign up today!</div>", unsafe_allow_html=True)

# --- SIDEBAR / FREEMIUM LOGIC ---
st.sidebar.title("Settings")
tier = st.sidebar.radio("Account Tier", ["Free", "Premium (Ad-Free)"])

asset = st.sidebar.selectbox("Select Asset", ["BTC/USD", "ETH/USD", "SOL/USD"])
stress_test = st.sidebar.checkbox("🔥 Enable Stress Period (Nov 2022)")

# --- MAIN DASHBOARD ---
st.title("🚀 Crypto Portfolio Backtester")

if tier == "Free":
    st.warning("You are on the Free Tier. Data is limited to Daily intervals.")

# Load Data (Placeholder for CSV or API call)
# df = pd.read_csv('btc_data.csv') 

if st.button("Run Strategy"):
    # Perform logic here...
    st.success(f"Backtest Complete for {asset}")
    
    # Display Results
    col1, col2, col3 = st.columns(3)
    col1.metric("Final Equity", "$12,450", "+24.5%")
    col2.metric("Sharpe Ratio", "1.82")
    col3.metric("Max Drawdown", "-12.4%")

    if stress_test:
        st.error("Stress Test Result: Strategy lost 8% during the FTX crash.")

# Inject Ads
show_ads(tier)
