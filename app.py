import streamlit as st
import pickle
import pandas as pd
import requests
import time

from requests.exceptions import ConnectionError, Timeout

# Reuse one connection instead of opening a new one every call
session = requests.Session()

@st.cache_data(show_spinner=False)
def fetch_poster(movie_id):
    url = 'https://api.themoviedb.org/3/movie/{}?api_key=6f80a16a8388e1f7cecca2feaae396ef&language=en-US'.format(movie_id)

    for attempt in range(3):
        try:
            response = session.get(url, timeout=10)
            data = response.json()

            if data.get('poster_path'):
                return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
            return None

        except (ConnectionError, Timeout):
            time.sleep(1.5)

    return None  # give up after 3 tries, don't crash the app


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]]['id']

        recommended_movies.append(
            movies.iloc[i[0]]['title']
        )

        recommended_movies_posters.append(
            fetch_poster(movie_id)
        )

    return recommended_movies, recommended_movies_posters


movies_dict = pickle.load(
    open('movies.pkl', 'rb')
)

movies = pd.DataFrame(movies_dict)

similarity = pickle.load(
    open('similarity.pkl', 'rb')
)
# ---------- UI ----------

st.markdown("""
<style>
.stApp {
    background-color: #141414;
}

h1 {
    color: white !important;
}

.stSelectbox label {
    color: white !important;
}

.stButton button {
    background-color: #e50914;
    color: white;
    border: none;
}

.stButton button:hover {
    background-color: #b20710;
    color: white;
}

.movie-title {
    text-align: center;
    color: white;
    font-size: 15px;
    font-weight: 600;
    height: 45px;
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>
""", unsafe_allow_html=True)


st.title("🎬 Movie Recommender")

selected_movie_name = st.selectbox(
    "Select a movie",
    movies['title'].values
)

if st.button("▶ Recommend"):

    names, posters = recommend(selected_movie_name)

    cols = st.columns(5)

    for col, name, poster in zip(cols, names, posters):

        with col:
            st.markdown(
                f'<div class="movie-title">{name}</div>',
                unsafe_allow_html=True
            )

            if poster:
                st.image(
                    poster,
                    use_container_width=True
                )