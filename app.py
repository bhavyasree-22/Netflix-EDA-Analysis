import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Netflix Data Analysis Dashboard")

df = pd.read_csv("netflix_titles.csv")

# Movies vs TV Shows
type_counts = df['type'].value_counts()

fig = px.pie(
    values=type_counts.values,
    names=type_counts.index,
    title="Movies vs TV Shows Distribution"
)

st.plotly_chart(fig)

# Ratings Distribution
rating_counts = df['rating'].value_counts()

fig2 = px.bar(
    x=rating_counts.index,
    y=rating_counts.values,
    title="Ratings Distribution"
)

st.plotly_chart(fig2)
