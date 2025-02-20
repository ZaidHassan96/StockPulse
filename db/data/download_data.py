import yfinance as yf
import pandas as pd



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




stock_list_data = []

# Looping through the list and downloading each companies data by using the yfinance.download function which uses the symbol i.e "AMZN" for the company Amazon.
for symbol, name in stocks:
    data = yf.download(symbol, period="1y")
    data["Company"] = name
    data.reset_index(inplace=True)
    data.columns = data.columns.droplevel(1)
    data.columns.name = None
    stock_list_data.append(data)





stock_list_data = pd.concat(stock_list_data)


# data = pd.read_csv('stocks.csv')


stock_list_data['Daily_Return'] = (((stock_list_data['Close'] - stock_list_data['Open']) / stock_list_data['Open']) * 100)

stock_list_data['SMA_200'] = stock_list_data['Close'].rolling(window=200).mean()

stock_list_data['Volatility'] = stock_list_data['Daily_Return'].rolling(window=50).std()

stock_list_data['Daily_Return'] = stock_list_data['Daily_Return'].round(2).astype(str) + '%'

stock_list_data.round(2).to_csv("stocks.csv", index=False)