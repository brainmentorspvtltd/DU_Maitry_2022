import streamlit as st

st.title("This is streamlit demo...")
st.write("Hello This is my first app...")

value = st.slider("slide")
st.write(value, "squared is :", value ** 2)