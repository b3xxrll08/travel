import requests
import pandas
import sqlalchemy

url = 'https://api.coincap.io/v2/assets/'
header={"Content-Type":"application/json",
        "Accept-Encoding":"deflate"}

response = requests.get(url, headers=header)
print(response)

responseData = response.json()
#print(responseData)

df = pandas.json_normalize(responseData, 'data')
#print(df)

engine=sqlalchemy.create_engine('mssql+pyodbc://./DWH?driver=SQL+Server+Native+Client+11.0')
df.to_sql(name='FactCrypto',con=engine,index=False, if_exists='fail')