import streamlit as st



back_home = st.button("Back Home Page")

if back_home:
    st.switch_page("../Read_Db_Sql/Home.py")

st.title("Chat with your Database")
