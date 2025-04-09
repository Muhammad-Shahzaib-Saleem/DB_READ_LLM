import pandas as pd
import sqlalchemy
from dotenv import load_dotenv
import os


load_dotenv()

# def db_read():
engine = sqlalchemy.create_engine(os.getenv("CONNEC_URL"))

pd.set_option('display.max_columns', None)

df = pd.read_sql_table("movie",engine)
print("All data: ",df)
df.to_csv("netflix_db.csv")
df.to_json("movie.json")


