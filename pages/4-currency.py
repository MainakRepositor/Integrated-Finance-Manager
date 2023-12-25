import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

# Function to fetch currency exchange rate data using Yahoo Finance
def get_currency_data(symbol):
    currency_data = yf.Ticker(symbol)
    historical_data = currency_data.history(period="max")
    return historical_data

# Function to display charts for currency performance
def display_performance_charts(data):
    st.subheader('Currency Performance Charts')
    
    # Line chart for historical exchange rates
    st.write('### Historical Exchange Rates')
    plt.figure(figsize=(10, 6))
    plt.plot(data['Close'])
    plt.title('Historical Exchange Rates')
    plt.xlabel('Date')
    plt.ylabel('Exchange Rate')
    st.pyplot(plt)

# Function to calculate expected returns
def calculate_expected_returns(investment_amount, investment_period, end_date, currency_data):
    # Extract date component from the index
    currency_data['Date'] = currency_data.index.date

    # Calculate percentage change over the investment period
    start_date = currency_data['Date'].iloc[0]
    end_date = pd.Timestamp(end_date).date()
    selected_data = currency_data[(currency_data['Date'] >= start_date) & (currency_data['Date'] <= end_date)]
    returns = selected_data['Close'].pct_change().dropna()

    # Calculate expected returns based on inputs
    expected_return = investment_amount * ((1 + np.mean(returns)) ** investment_period) - investment_amount
    return expected_return

# Function to run the Streamlit app
def main():
    st.title('Currency Performance Analysis')
    st.sidebar.title('Select Investment Parameters')

    # Sliders for investment parameters
    investment_amount = st.sidebar.slider('Basic Investment Amount (₹)', 1000, 100000, 10000, 1000)
    investment_period = st.sidebar.slider('Investment Period (Years)', 1, 10, 5, 1)

    # Date picker for investment period end date
    end_date = st.sidebar.date_input('Select Investment End Date', value=pd.Timestamp.now())

    st.sidebar.subheader('Expected Returns')
    try:
        # Sample list of 20 different currency symbols
        currency_symbols = [
            'INR', 'EUR', 'GBP', 'JPY', 'CAD', 'HKD',
            'CHF', 'ZAR', 'AUD', 'MXN', 'NZD', 'SGD',
            'KRW', 'BRL', 'TRY', 'NOK', 'SEK', 'RUB',
            'TWD', 'PLN'
        ]

        selected_symbol = st.sidebar.selectbox('Select a Currency Symbol', currency_symbols)
        currency_data = get_currency_data(selected_symbol)

        if not currency_data.empty:
            st.write(f'### {selected_symbol} Historical Data')
            st.write(currency_data.head())

            display_performance_charts(currency_data)

            expected_return = calculate_expected_returns(
                investment_amount, investment_period, end_date, currency_data
            )
            st.sidebar.write(f'Expected Returns after {investment_period} years: ₹{expected_return:.2f}')

        else:
            st.warning('No data available for the selected currency symbol.')
    except Exception as e:
        st.error('Error occurred while fetching data.')
        st.error(str(e))

if __name__ == "__main__":
    main()
