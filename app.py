import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# ---------- Custom Theme ----------
st.markdown("""
<style>
body {
    background-color: black;
    color: white;
}
h1,h2,h3 {
    color: #E50914;
}
</style>
""", unsafe_allow_html=True)

st.title("NETFLIX DATA ANALYSIS DASHBOARD")

# ---------- Load Dataset ----------
df = pd.read_csv("netflix_titles.csv", encoding="latin1")

# ---------- Clean Data ----------
df['country'] = df['country'].fillna("Unknown")
df['listed_in'] = df['listed_in'].fillna("Unknown")

# ---------- Top Row ----------
col1, col2, col3 = st.columns([2,1,1])

# ----- Map -----
with col1:
    st.subheader("Total Movies & TV Shows by Country")

    country = df['country'].str.split(',').explode().value_counts().reset_index()
    country.columns = ['country','count']

    fig = px.choropleth(
        country,
        locations="country",
        locationmode="country names",
        color="count",
        color_continuous_scale="Reds",
        template="plotly_dark"
    )

    st.plotly_chart(fig,use_container_width=True)

# ----- Ratings -----
with col2:
    st.subheader("Ratings")

    ratings = df['rating'].value_counts().head(10)

    fig2 = px.bar(
        x=ratings.index,
        y=ratings.values,
        color_discrete_sequence=["red"],
        template="plotly_dark"
    )

    st.plotly_chart(fig2,use_container_width=True)

# ----- Movie vs TV -----
with col3:
    st.subheader("Movies & TV Shows Distribution")

    type_counts = df['type'].value_counts()

    fig3 = px.pie(
        values=type_counts.values,
        names=type_counts.index,
        color_discrete_sequence=["red","salmon"],
        template="plotly_dark"
    )

    st.plotly_chart(fig3,use_container_width=True)

# ---------- Bottom Row ----------
col4, col5 = st.columns(2)

# ----- Top Genres -----
with col4:
    st.subheader("Top 10 Genre")

    genres = df['listed_in'].str.split(',').explode().value_counts().head(10)

    fig4 = px.bar(
        x=genres.values,
        y=genres.index,
        orientation='h',
        color_discrete_sequence=["red"],
        template="plotly_dark"
    )

    st.plotly_chart(fig4,use_container_width=True)

# ----- Growth Over Years -----
with col5:
    st.subheader("Total Movies & TV Shows by Years")

    df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')

    growth = df.groupby(['release_year','type']).size().reset_index(name='count')

    fig5 = px.area(
        growth,
        x="release_year",
        y="count",
        color="type",
        color_discrete_sequence=["red","salmon"],
        template="plotly_dark"
    )

    st.plotly_chart(fig5,use_container_width=True)
