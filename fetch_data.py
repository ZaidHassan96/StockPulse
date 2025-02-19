import streamlit as st
import pandas as pd
import psycopg2
import seaborn as sns
import matplotlib.pyplot as plt
from db_config import connection


def fetch_stock_data(company):

    try:
        query = f"SELECT close, open, date FROM stock_data WHERE company = '{company}';"
        data_frame = pd.read_sql(query, connection)
        connection.close
        return data_frame
    
    except Exception as error:
        print(f"Error: {error}")


