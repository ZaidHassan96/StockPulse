from utils.fetch_data import fetch_stock_data
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


# # list of tuples containing company symbols and names.
stocks = [
    ("AAPL", "Apple Inc."),
    ("MSFT", "Microsoft Corp."),
    ("GOOGL", "Alphabet Inc. (Google)"),
    ("GOOG", "Alphabet Inc. (Google) - Class C"),
    ("AMZN", "Amazon.com, Inc."),
    ("NVDA", "NVIDIA Corporation"),
    ("META", "Meta Platforms, Inc. (Facebook)"),
    ("TSLA", "Tesla Inc."),
    ("TSM", "Taiwan Semiconductor Manufacturing Company (TSMC)"),
    ("BRK-A", "Berkshire Hathaway Inc. - Class A"),
    ("BRK-B", "Berkshire Hathaway Inc. - Class B"),
    ("ADBE", "Adobe Inc."),
    ("INTC", "Intel Corporation"),
    ("ASML", "ASML Holding"),
    ("ORCL", "Oracle Corporation"),
    ("CRM", "Salesforce, Inc."),
    ("AMD", "Advanced Micro Devices"),
    ("QCOM", "Qualcomm Incorporated"),
    ("PYPL", "PayPal Holdings, Inc."),
    ("SPOT", "Spotify Technology S.A."),
    ("ZM", "Zoom Video Communications"),
    ("NOW", "ServiceNow, Inc.")
]

st.title('Stock Price Trend Visualization')

# Dropdown for selecting a stock symbol
stock_company = st.selectbox('Select a company', [stock[1] for stock in stocks])  # Add your stock symbols here

print(stock_company)



# Streamlit UI
st.title('Stock Price Trend Visualization')


# Fetch the data based on the selected stock symbol
if stock_company:
    df = fetch_stock_data(stock_company)
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # Display the raw data (optional)
    st.subheader('Raw Data')
    st.write(df)

    # Plotting the data
    st.subheader(f'{stock_company} Price Trend')

    # Check if the DataFrame has data
if not df.empty:
    # Set up the seaborn style (optional)
    # sns.set(style="darkgrid")

    # Create a plot with matplotlib and seaborn
    plt.figure(figsize=(10, 6))

    # Plot 'Open' and 'Close' prices on the same graph
    sns.lineplot(x='date', y='open', data=df, label='Open Price', color='green')
    sns.lineplot(x='date', y='close', data=df, label='Close Price', color='red')

    # Add title and labels
    plt.title(f'{stock_company} Stock Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    
    # Rotate the x-axis labels for better readability
    plt.xticks(rotation=45)

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))  # This will show 'Jan 2025', 'Feb 2025', etc.
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())  # This will set the x-axis tick marks to months

    # Display the plot in the Streamlit app
    st.pyplot(plt)

else:
    st.write(f"No data available for {stock_company}")