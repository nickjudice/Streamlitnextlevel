#Creating new streamlit practice session
import pandas as pd
import streamlit as st
import numpy as np


st.title("Streamlit 101: An in-depth introduction")
st.markdown("Welcome to this in-depth introduction to learning streamlit")
st.header("Nick's practice")
st.markdown("One day I'll be a wizard at this.")

def main():
  
  if __name__ == '__main__':
    main()
    
@st.cache_data
def data_load(nrows):
  df = pd.read_csv(DATA_URL, nrows=nrows)
  lower_str = lambda x: str(x).lower()
  df.rename(lower_str, axis='columns', inplace=True)
  df['date/time'] = pd.to_datetime(df['date/time'])
  return df

df = data_load(1000)
