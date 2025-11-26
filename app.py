import streamlit as st
import pandas as pd
import numpy as np
import joblib

@st.cache_resource
def load_models():
    try:
        model_knn = joblib.load("models/knn_model.pkl")
        rating_matrix = joblib.load("models/rating_matrix.pkl")
        movie_index = joblib.load("models/movie_index.pkl")
        movies = joblib.load("models/movies.pkl")
        cosine_sim = np.load("models/cosine_sim.npy")
        return model_knn, rating_matrix, movies, cosine_sim, movie_index
    except Exception as e:
        st.error(f"Error loading models: {e}")
        return None, None, None, None, None
