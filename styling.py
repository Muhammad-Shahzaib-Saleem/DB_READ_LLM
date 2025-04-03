import streamlit as st

def load_button_style():
    return """
    <style>
        .stButton>button {
            width: 200px;
            height: 50px;
            font-size: 20px;
            border-radius: 10px;  /* Optional: Add rounded corners */
            background-color: #4CAF50;  /* Optional: Green background */
            color: white;
            text-color: blue;
        }
        .stTitle>title{
            color:blue;
        }
    </style>
    """