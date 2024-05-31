import streamlit as st

st.write('Hello World')
x = st.text_input('Favourite movie?')
st.write(f'Your favourite movie is {x}')
# st.link_button('Chart', url='/pages/2_charts.py')