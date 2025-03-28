import pandas as pd
import sqlalchemy
import pymysql
import pymssql
engine = sqlalchemy.create_engine("mssql+pymssql://SA:CodeWithShahzaib12@localhost:1433/master")

pd.set_option('display.max_columns', None)

df = pd.read_sql_table("movie",engine)

df.to_csv("netflix_db.csv")
df.to_json("movie.json")


print(df.head(10))