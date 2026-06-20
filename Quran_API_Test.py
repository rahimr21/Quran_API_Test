import requests
import pandas as pd
import sqlalchemy as db

BASE_URL = 'http://api.alquran.cloud/v1/'


#getting API data
surah = input('Enter Surah Number: ')
response = requests.get(BASE_URL + 'surah/' + surah)

print(response.json())

#converting api json to dataframe
dataframe_name = pd.DataFrame.from_dict(response.json())

#creating engine and saving to sql
engine = db.create_engine('sqlite:///data_base_name.db')

dataframe_name.to_sql('table_name', con=engine, if_exists='replace', index=False)

#quering data and printing
with engine.connect() as connection:
   query_result = connection.execute(db.text("SELECT * FROM table_name;")).fetchall()
   print(pd.DataFrame(query_result))
