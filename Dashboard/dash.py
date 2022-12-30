import streamlit as st
import pandas  as pd
import plotly.express as ex
import numpy as np

df = pd.read_csv("IPL Matches 2008-2020.csv")

st.set_page_config(
    page_title="IPL Dashboard",
    layout="wide"
)

# df.dropna(inplace=True)

st.title("Real time IPL Dashboard...")

df['date'] = pd.to_datetime(df['date'])
df['season'] = pd.to_datetime(df['date']).dt.year

filter = st.selectbox("Select the Season", pd.unique(df['season']))

df = df[df['season'] == filter]

fig_1, fig_2 = st.columns(2)
with fig_1:
    st.markdown("Number of wins")
    fig = ex.bar(df['winner'])
    st.write(fig)
with fig_2:
    st.markdown("Number of matches in each venue")
    fig = ex.bar(df['venue'])
    st.write(fig)

fig_1, fig_2 = st.columns(2)
with fig_1:
    st.markdown("Toss decision")
    values = pd.value_counts(df['toss_decision'])
    fig = ex.pie(df['toss_decision'], values=values, names=['Field','Bat'])
    st.write(fig)
with fig_2:
    st.markdown("Number of matches in each season")
    fig = ex.bar(df['season'])
    st.write(fig)

st.dataframe(df)