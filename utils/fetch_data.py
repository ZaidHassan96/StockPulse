import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from db.db_config import connection




def fetch_stock_data(company):

    try:
        query = f"SELECT close, open, date, daily_return, volatility, sma_200, volume FROM stock_data WHERE company = '{company}';"
        data_frame = pd.read_sql(query, connection)
        connection.close
        return data_frame
    
    except Exception as error:
        print(f"Error: {error}")


