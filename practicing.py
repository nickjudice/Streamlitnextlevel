#Creating new streamlit practice session
import pandas as pd
import streamlit as st
import plotly.express as px

@st.cache_data
def get_data():
    url = "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-09-12/visualisations/listings.csv"
    return pd.read_csv(url)

df = get_data()

st.title("Streamlit 101: An in-depth introduction")
st.markdown("Welcome to this in-depth introduction to learning streamlit")
st.header("Nick's practice")
st.markdown("One day I'll be a wizard at this.")

st.dataframe(df.head())
