import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def build_files():
    # Load movie data
    movies = pd.read_csv("tmdb_5000_movies.csv")
    credits = pd.read_csv("tmdb_5000_credits.csv")

    # Merge datasets
    movies = movies.merge(credits, on="title")

    # Create movie dictionary (simple version)
    movie_dict = movies.to_dict()

    # Example similarity (replace with your actual logic if different)
    similarity = cosine_similarity(
        movies.select_dtypes(include=["number"]).fillna(0)
    )

    # Save files
    pickle.dump(movie_dict, open("movie_dict.pkl", "wb"))
    pickle.dump(similarity, open("similarity.pkl", "wb"))

    print("PKL files created successfully")

# IMPORTANT: prevent auto execution on import
if __name__ == "__main__":
    build_files()
