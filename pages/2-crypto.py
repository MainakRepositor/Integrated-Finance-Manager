import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Function to fetch cryptocurrency data
def get_crypto_data(symbols, start_date, end_date):
    data = yf.download(symbols, start=start_date, end=end_date)
    return data['Close']

# Function to display cryptocurrency data and performance
def display_crypto_data(crypto_data):
    st.subheader("Cryptocurrency Data:")
    st.write(crypto_data)

    st.subheader("Cryptocurrency Performance:")
    st.line_chart(crypto_data)

# Function to calculate portfolio value
def calculate_portfolio_value(allocations, crypto_data):
    portfolio_value = allocations.dot(crypto_data.iloc[-1])
    return portfolio_value

# Function to display portfolio summary
def display_portfolio_summary(portfolio_value, allocations):
    st.subheader("Portfolio Summary:")
    st.write(f"Total Portfolio Value: ₹{portfolio_value:,.2f}")

    st.subheader("Portfolio Allocations:")
    st.write(allocations)

# Function to display pie chart for allocations
def display_pie_chart(allocations):
    plt.figure(figsize=(8, 8))
    plt.pie(allocations.values, labels=allocations.index, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    st.subheader("Portfolio Allocation Breakdown:")
    st.pyplot(plt)

# Function to check portfolio rise and display alert
def check_portfolio_rise(portfolio_value, alert_threshold):
    if portfolio_value > alert_threshold:
        st.subheader("Portfolio Alert:")
        st.warning(f"Your portfolio value has risen above ₹{alert_threshold:,.2f}!")

# Streamlit App for Cryptocurrencies
def main():
    st.title("Cryptocurrency Portfolio Manager")

    # Sidebar for user input
    st.sidebar.header("User Input:")
    symbols = st.sidebar.text_input("Enter Cryptocurrency Symbols (comma-separated, e.g., BTC-USD,ETH-USD):", "BTC-USD,ETH-USD").upper().split(',')
    start_date = st.sidebar.date_input("Start Date:", datetime(2020, 1, 1))
    end_date = st.sidebar.date_input("End Date:", datetime.now())

    # Fetch cryptocurrency data for multiple symbols
    crypto_data = get_crypto_data(symbols, start_date, end_date)

    # Display cryptocurrency data and performance
    display_crypto_data(crypto_data)

    # User-defined portfolio allocations
    st.sidebar.header("Portfolio Allocations:")
    alloc_input = {}
    for crypto_symbol in crypto_data.columns:
        alloc_input[crypto_symbol] = st.sidebar.slider(f"Allocation for {crypto_symbol} (%)", 0, 100, 10)

    allocations = pd.Series(alloc_input) / 100

    # Calculate and display portfolio value
    portfolio_value = calculate_portfolio_value(allocations, crypto_data)
    display_portfolio_summary(portfolio_value, allocations)

    # Display pie chart for allocations
    display_pie_chart(allocations)

    # Check portfolio rise and display alert
    alert_threshold = st.sidebar.number_input("Set Portfolio Alert Threshold (₹):", value=10000.0, step=100.0)
    check_portfolio_rise(portfolio_value, alert_threshold)

if __name__ == "__main__":
    main()
