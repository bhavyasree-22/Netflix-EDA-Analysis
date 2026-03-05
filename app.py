import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# Netflix Theme
st.markdown("""
<style>
body {
    background-color: #000000;
    color: white;
}
h1,h2,h3{
color:#E50914;
}
</style>
""", unsafe_allow_html=True)

st.title("NETFLIX DATA ANALYSIS DASHBOARD")

# Load dataset
df = pd.read_csv("netflix_titles.csv",encoding="latin1")

# Clean columns
df['country'] = df['country'].fillna("Unknown")
df['listed_in'] = df['listed_in'].fillna("Unknown")

# -------- TOP ROW --------
col1,col2,col3 = st.columns([2,1,1])

# Map
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

    fig.update_layout(
        paper_bgcolor='black',
        plot_bgcolor='black'
    )

    st.plotly_chart(fig,use_container_width=True)


# Ratings
with col2:

    st.subheader("Ratings")

    rating = df['rating'].value_counts().head(10)

    fig2 = px.bar(
        x=rating.index,
        y=rating.values,
        color_discrete_sequence=['#E50914'],
        template="plotly_dark"
    )

    fig2.update_layout(
        paper_bgcolor='black',
        plot_bgcolor='black'
    )

    st.plotly_chart(fig2,use_container_width=True)


# Movie vs TV bubble
with col3:

    st.subheader("Movies & TV Shows Distribution")

    type_counts = df['type'].value_counts().reset_index()
    type_counts.columns=['type','count']

    fig3 = px.scatter(
        type_counts,
        x=["Movie","TV Show"],
        y=[1,1],
        size="count",
        color="type",
        color_discrete_sequence=["red","#ff7f7f"],
        size_max=200,
        template="plotly_dark"
    )

    fig3.update_layout(
        showlegend=True,
        paper_bgcolor='black'
    )

    st.plotly_chart(fig3,use_container_width=True)

# -------- BOTTOM ROW --------
col4,col5 = st.columns(2)

# Genres
with col4:

    st.subheader("Top 10 Genre")

    genres = df['listed_in'].str.split(',').explode().value_counts().head(10)

    fig4 = px.bar(
        x=genres.values,
        y=genres.index,
        orientation='h',
        color_discrete_sequence=['red'],
        template="plotly_dark"
    )

    fig4.update_layout(
        paper_bgcolor='black',
        plot_bgcolor='black'
    )

    st.plotly_chart(fig4,use_container_width=True)


# Growth
with col5:

    st.subheader("Total Movies & TV Shows by Years")

    df['release_year']=pd.to_numeric(df['release_year'],errors='coerce')

    growth = df.groupby(['release_year','type']).size().reset_index(name='count')

    fig5 = px.area(
        growth,
        x="release_year",
        y="count",
        color="type",
        color_discrete_sequence=['red','#ff7f7f'],
        template="plotly_dark"
    )

    fig5.update_layout(
        paper_bgcolor='black',
        plot_bgcolor='black'
    )

    st.plotly_chart(fig5,use_container_width=True)
