import streamlit as st
import pandas as pd
import numpy as np

samples = st.number_input(label='Enter no. of samples:',min_value=1,value=20)

chart_data = pd.DataFrame(
    np.random.randn(samples,3),
    columns = ['a', 'b', 'c']
)

st.bar_chart(chart_data)
st.line_chart(chart_data)
