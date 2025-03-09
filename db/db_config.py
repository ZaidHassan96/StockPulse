# import psycopg2
# from pathlib import Path
# import os
# from dotenv import load_dotenv


# # Load environment variables from .env file
# load_dotenv()

# try:
#     connection = psycopg2.connect(
#         dbname=os.getenv("DB_NAME"),
#         user=os.getenv("DB_USER"),
#         password=os.getenv("DB_PASSWORD"),
#         host=os.getenv("DB_HOST"),
#         port=os.getenv("DB_PORT")
#     )
    
# except Exception as error:
#     print(f"Error: {error}")

import psycopg2
import os
from dotenv import load_dotenv
from pathlib import Path
import streamlit as st



production = True

# Check if running on Streamlit Cloud
if production:
    # Running on Streamlit Cloud (use st.secrets)
    DB_NAME = st.secrets["database"]["DB_NAME"]
    DB_USER = st.secrets["database"]["DB_USER"]
    DB_PASSWORD = st.secrets["database"]["DB_PASSWORD"]
    DB_HOST = st.secrets["database"]["DB_HOST"]
    DB_PORT = st.secrets["database"]["DB_PORT"]
else:
    # Running Locally (use .env file)
    load_dotenv()
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")

# Connect to PostgreSQL
try:
    connection = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    print("Database connection successful!")
except Exception as error:
    print(f"Error: {error}")
