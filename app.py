import streamlit as st
import pandas as pd
import plotly.express as px

# Page settings
st.set_page_config(page_title="Netflix Dashboard", layout="wide")

# Custom Netflix style
st.markdown("""
<style>
body {background-color: black; color: white;}
h1,h2,h3 {color:#E50914;}
</style>
""", unsafe_allow_html=True)

st.title("NETFLIX DATA ANALYSIS DASHBOARD")

# Load dataset
df = pd.read_csv("netflix_titles.csv", encoding="latin1")

# ---------- Top Section ----------
col1, col2, col3 = st.columns(3)

# Ratings chart
with col1:
    st.subheader("Ratings")
    ratings = df['rating'].value_counts().head(10)
    fig = px.bar(
        x=ratings.index,
        y=ratings.values,
        color_discrete_sequence=["#E50914"]
    )
    fig.update_layout(paper_bgcolor="black", plot_bgcolor="black", font_color="white")
    st.plotly_chart(fig, use_container_width=True)

# Movie vs TV distribution
with col2:
    st.subheader("Movies & TV Shows Distribution")
    type_counts = df['type'].value_counts()
    fig2 = px.pie(
        values=type_counts.values,
        names=type_counts.index,
        color_discrete_sequence=["#E50914","#FF6B6B"]
    )
    fig2.update_layout(paper_bgcolor="black", font_color="white")
    st.plotly_chart(fig2, use_container_width=True)

# Country distribution
with col3:
    st.subheader("Top Countries")
    country = df['country'].str.split(',').explode().value_counts().head(10)
    fig3 = px.bar(
        x=country.values,
        y=country.index,
        orientation='h',
        color_discrete_sequence=["#E50914"]
    )
    fig3.update_layout(paper_bgcolor="black", plot_bgcolor="black", font_color="white")
    st.plotly_chart(fig3, use_container_width=True)

# ---------- Bottom Section ----------
col4, col5 = st.columns(2)

# Top Genres
with col4:
    st.subheader("Top 10 Genres")
    genres = df['listed_in'].str.split(',').explode().value_counts().head(10)
    fig4 = px.bar(
        x=genres.values,
        y=genres.index,
        orientation='h',
        color_discrete_sequence=["#E50914"]
    )
    fig4.update_layout(paper_bgcolor="black", plot_bgcolor="black", font_color="white")
    st.plotly_chart(fig4, use_container_width=True)

# Content growth
with col5:
    st.subheader("Total Movies & TV Shows by Years")
    df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')
    growth = df.groupby(['release_year','type']).size().reset_index(name='count')

    fig5 = px.area(
        growth,
        x="release_year",
        y="count",
        color="type",
        color_discrete_sequence=["#E50914","#FF6B6B"]
    )

    fig5.update_layout(paper_bgcolor="black", plot_bgcolor="black", font_color="white")
    st.plotly_chart(fig5, use_container_width=True)
