import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Function to fetch stock data for a list of symbols
def get_stock_data(symbols, start_date, end_date):
    data = yf.download(symbols, start=start_date, end=end_date)['Adj Close']
    return data

# Function to display stock data and performance
def display_stock_data(stock_data):
    st.subheader("Stock Data:")
    st.write(stock_data)

    st.subheader("Stock Performance:")
    st.line_chart(stock_data)

# Function to calculate portfolio value
def calculate_portfolio_value(allocations, stock_data):
    portfolio_value = allocations.dot(stock_data.iloc[-1])
    return portfolio_value

# Function to display portfolio summary
def display_portfolio_summary(portfolio_value, allocations):
    st.subheader("Portfolio Summary:")
    st.write(f"Total Portfolio Value: ${portfolio_value:,.2f}")

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
        st.success(f"Your portfolio value has risen above ₹{alert_threshold:,.2f}!")

# Streamlit App for Stock Exchanges
def main():
    st.title("Stock Exchange Portfolio Manager")

    # Sidebar for user input
    st.sidebar.header("User Input:")
    symbols = st.sidebar.text_area("Enter Stock Symbols (comma-separated, e.g., AAPL,GOOGL,MSFT):", "AAPL,GOOGL,MSFT").upper().split(',')
    start_date = st.sidebar.date_input("Start Date:", datetime(2020, 1, 1))
    end_date = st.sidebar.date_input("End Date:", datetime.now())

    # Fetch stock data for multiple symbols
    stock_data = get_stock_data(symbols, start_date, end_date)

    # Display stock data and performance
    display_stock_data(stock_data)

    # User-defined portfolio allocations
    st.sidebar.header("Portfolio Allocations:")
    alloc_input = {}
    for stock_symbol in stock_data.columns:
        alloc_input[stock_symbol] = st.sidebar.slider(f"Allocation for {stock_symbol} (%)", 0, 100, 10)

    allocations = pd.Series(alloc_input) / 100

    # Calculate and display portfolio value
    portfolio_value = calculate_portfolio_value(allocations, stock_data)
    display_portfolio_summary(portfolio_value, allocations)

    # Display pie chart for allocations
    display_pie_chart(allocations)

    # Check portfolio rise and display alert
    alert_threshold = st.sidebar.number_input("Set Portfolio Alert Threshold (₹):", value=100.0, step=100.0)
    check_portfolio_rise(portfolio_value, alert_threshold)

if __name__ == "__main__":
    main()
