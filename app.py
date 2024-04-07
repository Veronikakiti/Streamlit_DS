import streamlit as st
import pandas as pd

st.header('Цены на недвижимость в России')
PATH_DATA = "data/all_v2.csv"

def load_data(path):
    """Load data from path"""
    data = pd.read_csv(path)
    data = data.sample(5000)
    return data

df = load_data(PATH_DATA)
st.write(df[:5])