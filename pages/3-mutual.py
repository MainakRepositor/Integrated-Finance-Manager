import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

# Function to fetch mutual fund data using Yahoo Finance
def get_mutual_fund_data(symbol):
    fund_data = yf.Ticker(symbol)
    historical_data = fund_data.history(period="max")
    return historical_data

# Function to display charts for fund performance
def display_performance_charts(data):
    st.subheader('Fund Performance Charts')
    
    # Line chart for historical fund prices
    st.write('### Historical Prices')
    plt.figure(figsize=(10, 6))
    plt.plot(data['Close'])
    plt.title('Historical Fund Prices')
    plt.xlabel('Date')
    plt.ylabel('Price (₹)')
    st.pyplot(plt)

    # Candlestick chart for historical fund prices
    st.write('### Candlestick Chart')
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(data.index, data['Close'], label='Closing Price', color='blue')
    ax.fill_between(data.index, data['High'], data['Low'], color='grey', alpha=0.3)
    ax.set_xlabel('Date')
    ax.set_ylabel('Price (₹)')
    ax.set_title('Candlestick Chart')
    st.pyplot(fig)

# Function to calculate expected returns
def calculate_expected_returns(investment_amount, investment_period, fund_size, liquidity, end_date, fund_data):
    # Extract date component from the index
    fund_data['Date'] = fund_data.index.date

    # Calculate percentage change over the investment period
    start_date = fund_data['Date'].iloc[0]
    end_date = pd.Timestamp(end_date).date()
    selected_data = fund_data[(fund_data['Date'] >= start_date) & (fund_data['Date'] <= end_date)]
    returns = selected_data['Close'].pct_change().dropna()

    # Calculate expected returns based on inputs
    expected_return = investment_amount * ((1 + np.mean(returns)) ** investment_period) - investment_amount
    return expected_return

# Function to run the Streamlit app
def main():
    st.title('Mutual Fund Performance Analysis')
    st.sidebar.title('Select Investment Parameters')

    # Sliders for investment parameters
    investment_amount = st.sidebar.slider('Basic Investment Amount (₹)', 1000, 100000, 10000, 1000)
    investment_period = st.sidebar.slider('Investment Period (Years)', 1, 10, 5, 1)
    fund_size = st.sidebar.slider('Fund Size (₹)', 1000000, 100000000, 10000000, 1000000)
    liquidity = st.sidebar.slider('Liquidity (₹)', 100000, 10000000, 1000000, 100000)

    # Date picker for investment period end date
    end_date = st.sidebar.date_input('Select Investment End Date', value=pd.Timestamp.now())

    st.sidebar.subheader('Expected Returns')
    try:
        selected_symbol = st.sidebar.selectbox('Select a Mutual Fund Symbol', ['VTSAX', 'SPY', 'AGG', 'VTI', 'VFIAX'])
        fund_data = get_mutual_fund_data(selected_symbol)

        if not fund_data.empty:
            st.write(f'### {selected_symbol} Historical Data')
            st.write(fund_data.head())

            display_performance_charts(fund_data)

            expected_return = calculate_expected_returns(
                investment_amount, investment_period, fund_size, liquidity, end_date, fund_data
            )
            st.success(f'Expected Returns after {investment_period} years: ₹{expected_return:.2f}')

        else:
            st.warning('No data available for the selected symbol.')
    except Exception as e:
        st.error('Error occurred while fetching data.')
        st.error(str(e))

if __name__ == "__main__":
    main()
