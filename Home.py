from io import StringIO
import streamlit as st
import pandas as pd
import db_read

st.set_page_config("Home","🏛")
st.title("Netflix DB Reader")
st.caption("Data Source MS SQL")


on = st.toggle("DB LLM")


col1,col2 = st.columns(2)







if on:
    st.switch_page("pages/db_llm.py")

def read_db(file_path):
    file = None
    with open(file_path,"r") as f:
        file = f.read()
    return file



# file_path = "netflix_db.csv"
# read_csv = read_db(file_path)
#
# df = pd.read_csv(StringIO(read_csv))


df = db_read.df
# na_rows = df.isna().any(axis=1).sum()
# final_data = df.head(200)
st.write(df.head(200))
# st.write("Number of NA Values Rows",na_rows)