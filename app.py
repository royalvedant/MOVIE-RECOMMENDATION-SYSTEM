import pandas as pd
import streamlit as st
import pickle
import requests




st.markdown(
    """
    <style>
    .type-loop {
        margin-top: -30px;   /* 🔼 move up */
        overflow: hidden;
        white-space: nowrap;
        border-right: 3px solid #2ecc71;
        font-size: 28px;
        font-weight: 700;
        width: 0;
        animation:
            typing 2.5s steps(22, end) infinite,
            blink 0.7s step-end infinite,
            fadeSlide 1.2s ease-in-out;
    }

    @keyframes typing {
        0% { width: 0 }
        40% { width: 100% }
        60% { width: 100% }
        100% { width: 0 }
    }

    @keyframes blink {
        50% { border-color: transparent }
    }

    @keyframes fadeSlide {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>

    <div class="type-loop">
        DEVELOPED BY : <span style="color:#2ecc71;">VEDANT</span>
    </div>
            """,
    unsafe_allow_html=True
)






st.markdown(
    """
    <style>
    .title-gradient {
        text-align: center;
        margin-top: -30px;
        font-size: 48px;
        font-weight: 900;
        background: linear-gradient(
            270deg,
            #ff4b4b,
            #ffa534,
            #ffe234,
            #2ecc71,
            #3498db,
            #9b59b6
        );
        background-size: 400% 400%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradientMove 5s ease infinite;
    }

    @keyframes gradientMove {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    </style>

    <h1 class="title-gradient">
        🎬 MovieMood – Matches Your Vibe
    </h1>
    """,
    unsafe_allow_html=True
)









movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity= pickle.load(open('similarity.pkl','rb'))


#api-8265bd1679663a7ea12ac.168da84d2e8
#link
def fetch_posters(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    response = requests.get(url)
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data["poster_path"]


def recommend(movie, new_df):

    movie = movie.lower().strip()

    if movie not in new_df['title'].str.lower().values:
        st.error("Movie not found")
        return []

    idx = new_df[new_df['title'].str.lower() == movie].index[0]
    distances = similarity[idx]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:11]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_index = i[0]
        movie_id = new_df.iloc[movie_index].movie_id

        recommended_movies.append(new_df.iloc[movie_index].title)
        recommended_movies_posters.append(fetch_posters(movie_id))

    return recommended_movies, recommended_movies_posters






st.markdown("<br>", unsafe_allow_html=True)

selected_movies_name = st.selectbox(
    "WHAT YOU LIKE TO WATCH?",
    movies['title'].values,
)


if st.button("SEARCH"):
    names, posters = recommend(selected_movies_name, movies)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.markdown(
            f"<p style='white-space: nowrap; overflow: hidden; text-overflow: ellipsis;'>{names[0]}</p>",
            unsafe_allow_html=True
        )
        st.image(posters[0])

    with col2:
        st.markdown(
            f"<p style='white-space: nowrap; overflow: hidden; text-overflow: ellipsis;'>{names[1]}</p>",
            unsafe_allow_html=True
        )
        st.image(posters[1])

    with col3:
        st.markdown(
            f"<p style='white-space: nowrap; overflow: hidden; text-overflow: ellipsis;'>{names[2]}</p>",
            unsafe_allow_html=True
        )
        st.image(posters[2])

    with col4:
        st.markdown(
            f"<p style='white-space: nowrap; overflow: hidden; text-overflow: ellipsis;'>{names[3]}</p>",
            unsafe_allow_html=True
        )
        st.image(posters[3])

    with col5:
        st.markdown(
            f"<p style='white-space: nowrap; overflow: hidden; text-overflow: ellipsis;'>{names[4]}</p>",
            unsafe_allow_html=True
        )
        st.image(posters[4])

    with col1:
        st.markdown(
            f"<p style='white-space: nowrap; overflow: hidden; text-overflow: ellipsis;'>{names[5]}</p>",
            unsafe_allow_html=True
        )
        st.image(posters[5])

    with col2:
        st.markdown(
            f"<p style='white-space: nowrap; overflow: hidden; text-overflow: ellipsis;'>{names[6]}</p>",
            unsafe_allow_html=True
        )
        st.image(posters[6])

    with col3:
        st.markdown(
            f"<p style='white-space: nowrap; overflow: hidden; text-overflow: ellipsis;'>{names[7]}</p>",
            unsafe_allow_html=True
        )
        st.image(posters[7])

    with col4:
        st.markdown(
            f"<p style='white-space: nowrap; overflow: hidden; text-overflow: ellipsis;'>{names[8]}</p>",
            unsafe_allow_html=True
        )
        st.image(posters[8])

    with col5:
        st.markdown(
            f"<p style='white-space: nowrap; overflow: hidden; text-overflow: ellipsis;'>{names[9]}</p>",
            unsafe_allow_html=True
        )
        st.image(posters[9])


