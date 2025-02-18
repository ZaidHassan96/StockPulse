import pandas as pd




data = pd.read_csv('stocks.csv')


data['Daily_Return'] = (((data['Close'] - data['Open']) / data['Open']) * 100)

data['SMA_200'] = data['Close'].rolling(window=200).mean()

data['Volatility'] = data['Daily_Return'].rolling(window=50).std()

data['Daily_Return'] = data['Daily_Return'].round(2).astype(str) + '%'

data.round(2).to_csv("processed_stock_data.csv", index=False)


