import streamlit as st

st.write('Hello World')
x = st.text_input('Favourite movie?')
st.write(f'Your favourite movie is {x}')
# st.link_button('Chart', url='/pages/2_charts.py')

st.subheader(body='Demonstration of text writing in Streamlit', divider='violet')
md = st.text_area(label='Type in your markdown string (without quotes)',
                  value='*Happy* :rainbow[Streamlit-ing] :balloon:'
                )

st.code(f"""
import streamlit as st
st.markdown('''{md}''')
""")

st.markdown(md)
