import streamlit as st
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(
    page_title="Netflix Dashboard",
    layout="wide",
)

# Custom Netflix style
st.markdown("""
<style>
body {
    background-color: #000000;
    color: white;
}
h1, h2, h3 {
    color: #E50914;
}
</style>
""", unsafe_allow_html=True)

st.title("NETFLIX DATA ANALYSIS DASHBOARD")

# Load dataset
df = pd.read_csv("/netflix_titles.csv")

# Movies vs TV shows
type_counts = df['type'].value_counts()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Movies vs TV Shows Distribution")

    fig = px.pie(
        values=type_counts.values,
        names=type_counts.index,
        color_discrete_sequence=["#E50914", "#B20710"]
    )

    fig.update_layout(
        paper_bgcolor="black",
        plot_bgcolor="black",
        font_color="white"
    )

    st.plotly_chart(fig, use_container_width=True)


# Ratings distribution
with col2:

    st.subheader("Ratings Distribution")

    rating_counts = df['rating'].value_counts()

    fig2 = px.bar(
        x=rating_counts.index,
        y=rating_counts.values,
        color_discrete_sequence=["#E50914"]
    )

    fig2.update_layout(
        paper_bgcolor="black",
        plot_bgcolor="black",
        font_color="white"
    )

    st.plotly_chart(fig2, use_container_width=True)


# Top genres
st.subheader("Top Genres")

genre = df['listed_in'].str.split(',').explode().value_counts().head(10)

fig3 = px.bar(
    x=genre.values,
    y=genre.index,
    orientation='h',
    color_discrete_sequence=["#E50914"]
)

fig3.update_layout(
    paper_bgcolor="black",
    plot_bgcolor="black",
    font_color="white"
)

st.plotly_chart(fig3, use_container_width=True)
