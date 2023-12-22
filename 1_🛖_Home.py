import streamlit as st

st.set_page_config(page_title="Checker Home", page_icon="⭐️")

st.title('Dead Link Checker Website.')
st.sidebar.success('Please choose an option from the navigation bar above.')

st.subheader('About Us... ')
st.write('This website aims to find all of the deadlinks from a url provided by the user.')
st.write('It uses a recursive method to find the deadlinks, diving deep into the website from the provided depth value by the user.')

st.write('NEXT STOP: Please go to the Instructions option below to know how the Deadlink Checker works!')