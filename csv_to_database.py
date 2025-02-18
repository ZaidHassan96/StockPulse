import psycopg2
import csv
from pathlib import Path
import os
from dotenv import load_dotenv




# Load environment variables from .env file
load_dotenv()

# Connect to your PostgreSQL database
try:
    connection = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )
    
    cursor = connection.cursor()

# Drop table if already exists.
    drop_table = '''DROP TABLE IF EXISTS stock_data;'''

    cursor.execute(drop_table)



    # Create the table
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS stock_data (
        date VARCHAR(100),
        close FLOAT,
        high FLOAT,
        low FLOAT,
        open FLOAT,
        volume BIGINT,
        company VARCHAR(100),
        daily_return VARCHAR(20),
        sma_200 FLOAT,
        volatility Float
    );
    '''

    cursor.execute(create_table_query)


    print("Table 'stock_data' created successfully")


    path = Path('processed_stock_data.csv')
    lines = path.read_text().splitlines()

    reader = csv.reader(lines)
    header_row = next(reader)
   
    
    

    for index in range(len(lines)):
        lines[index] = lines[index].split(",")
        # Skips the first line which is a header.
        if index == 0:
            continue
        # Removes inc from certain lists as it was seperated into a seperate element because there was a comma inbetween it and the company name.
        if len(lines[index]) == 11:
            lines[index].pop(7)
        # Replaces empty sma_200 and volatility fields with Null and removes extra " that appeared in some company names.
        line = [item.replace('"', '') if item != '' else None for item in lines[index]]
        

        
        insert = '''INSERT INTO stock_data (date, close, high, low, open, volume, company, daily_return, sma_200, volatility) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
        cursor.execute(insert, (line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9]))
    
    print("inserted succesfully")
    

   
 

    connection.commit()  # Commit the changes to the database


except Exception as error:
    print(f"Error: {error}")
finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if connection:
        connection.close()
