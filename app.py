import pickle
import requests
import streamlit as st

def fetch_poster(movie_id):
    response = requests.get(
        "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(
            movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommended(movie):
    movie = movie.lower()
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:16]

    recommended_movies = []
    recommended_movies_posters = []
    for j in movies:
        movie_id = movies_list.iloc[j[0]].movie_id
        recommended_movies.append(movies_list.iloc[j[0]].title.title())
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters


movies_list = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')
option = st.selectbox(
    'How would you like to be connected?',
    movies_list['title'].values
)

if st.button('Recommend'):
    names, posters = recommended(option)
    col1, col2, col3= st.columns(3)
    with col1:
        for i in range(0,5):
            st.write(names[i])
            st.image(posters[i])

    with col2:
        for i in range(5, 10):
            st.write(names[i])
            st.image(posters[i])

    with col3:
        for i in range(10,15):
            st.write(names[i])
            st.image(posters[i])

