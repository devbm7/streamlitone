import streamlit as st
import pandas as pd

data = pd.read_csv('movies.csv')
st.write(data)