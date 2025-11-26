🎬 Movie Recommendation System – Streamlit Web App

A **Hybrid Movie Recommendation System** built using
**Content-Based Filtering + Collaborative Filtering (KNN)**,
fully deployable on **Streamlit Cloud using GitHub**.

No `scikit-surprise` needed — works smoothly in **Streamlit, Jupyter, Anaconda, PyCharm, Google Colab**.

---

## 🌐 Live Demo

🚀 **App Link:** *(Your Streamlit link will appear here after deployment)*
💻 GitHub Repository: *(Add your repo link here)*

---

## 🔍 Project Overview

This Movie Recommendation System suggests movies to users based on:

| Technique                  | Description                                       |
| -------------------------- | ------------------------------------------------- |
| 🎭 Content-Based Filtering | Recommends movies with similar genres             |
| 👥 Collaborative Filtering | Uses KNN to find similar users and suggest movies |
| 🔀 Hybrid Model            | Combines both recommendations for better accuracy |

This model uses the **MovieLens Dataset** and is ideal for:
✨ Mini projects | ✨ Final-year projects | ✨ Data Science Portfolio | ✨ Resume/LinkedIn Showcase

---

## 🛠️ Features

✔ Search movies & get similar content (Content-Based)
✔ Enter User ID to get user-based recommendations (Collaborative)
✔ Intelligent hybrid recommendation mode
✔ Zero dependency on `scikit-surprise`
✔ Auto-load dataset from hosted CSV
✔ Streamlit Web Interface with sidebar options

---

## 📁 Project Structure

```
movie-recommender-streamlit/
├── app.py                # Streamlit app UI
├── model_utils.py        # ML and recommendation logic
├── sample_data.py        # Loads dataset from hosted URLs
├── requirements.txt      # Required dependencies
├── README.md             # Documentation
├── models/ (optional)    # Pre-trained model files (if saved)
└── data/ (optional)      # Only if using local CSV (not needed for deployment)
```

---

## 🚀 How to Run Locally

### 📌 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 📌 2. Run Streamlit Web App

```bash
streamlit run app.py
```

### 📌 3. Open in browser

👉 [http://localhost:8501](http://localhost:8501)

---

## 📦 Deployment on Streamlit Cloud (GitHub)

1️⃣ Push this entire project to a **public GitHub repository**
2️⃣ Go to ➤ [https://share.streamlit.io](https://share.streamlit.io)
3️⃣ Click **Deploy an app**
4️⃣ Select repo → Choose `app.py` → Deploy 🚀
5️⃣ Get your **live app link!** 🎉

---

## 📊 Dataset Used

We use MovieLens dataset (loaded via online links):

| File          | Description                            |
| ------------- | -------------------------------------- |
| `movies.csv`  | Movie titles & genres                  |
| `ratings.csv` | User ratings (userId, movieId, rating) |

## 📸 Streamlit UI Preview

| Mode          | Description                              |
| ------------- | ---------------------------------------- |
| Content-Based | Enter movie title → Get similar movies   |
| Collaborative | Enter User ID → Get recommendations      |
| Hybrid Mode   | Combines both models for better accuracy |

---

## 📘 Recommendation Techniques

### 🎭 Content-Based Filtering

```python
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['genre_tokens'])
similarity = cosine_similarity(tfidf_matrix, tfidf_matrix)
```

---

### 👥 Collaborative Filtering (KNN)

```python
rating_matrix = ratings.pivot_table(index='userId', columns='movieId', values='rating').fillna(0)
knn = NearestNeighbors(metric='cosine', algorithm='brute')
knn.fit(rating_matrix)
```

---

### 🔀 Hybrid Recommendation (Combined Output)

```python
hybrid = pd.concat([content_rec, collab_rec]).drop_duplicates().head(n)
```
## 📌 Future Enhancements

🔹 Add Movie Posters using TMDB API
🔹 Deep Learning-based Recommendation (Neural CF)
🔹 Deploy using HuggingFace / Render / AWS
🔹 Add user login & watchlist feature

