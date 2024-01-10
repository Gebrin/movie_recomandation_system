import streamlit as st 
import pickle
import requests

movies = pickle.load(open("movies_list.pkl","rb"))
movie_list = movies['title'].values

similarity = pickle.load(open("similarity.pkl","rb"))


st.header("Movie Recommender System")
select_value = st.selectbox("Select Movie from Dropdown",movie_list)

def fetch_poster(movie_id):
     url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
     data=requests.get(url)
     data=data.json()
     poster_path = data['poster_path']
     full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
     return full_path

def recomandation(movie):
    if movie in movies['title'].values:
        index = movies[movies['title'] == movie].index[0]
        distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
        recommend_movie = []
        poster = []
        for i in distance[1:6]:
            movie_id = movies.iloc[i[0]].id
            recommend_movie.append(movies.iloc[i[0]]['title'])
            poster.append(fetch_poster(movie_id))
        return recommend_movie,poster
if st.button("Show Recommendation"):
    movie_name, movie_poster = recomandation(select_value)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])
