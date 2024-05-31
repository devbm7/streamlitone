import streamlit as st
import pandas as pd

st.title('Movies Dataset')

st.header('A _look_ at the dataset of :blue[movies]',divider='rainbow')
st.markdown('*Source* is Kaggle, data from :red[rotten tomatoes]')
data = pd.read_csv('movies.csv')
st.write(data)
