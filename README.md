🎬 Movie Recommender System

A content-based movie recommendation system built using Python, Machine Learning, and Streamlit. The application recommends movies based on the similarity between their features.

🚀 Live Demo

🎬 "Try the Movie Recommender" (https://movie-recommender-system-4uijupx4kpecv7mbcal3af.streamlit.app/)

📌 About the Project

In this project, I built a movie recommendation system that suggests 5 similar movies based on the movie selected by the user.

I processed the movie dataset, combined relevant movie information into features, and used Cosine Similarity to find movies that are most similar to the selected movie.

The recommendation results are displayed through a simple Netflix-inspired Streamlit interface.

🔄 How It Works

Movie Dataset
     ↓
Data Preprocessing
     ↓
Feature Combination
     ↓
Similarity Calculation
     ↓
Find Similar Movies
     ↓
Top 5 Recommendations

When a user selects a movie, the system finds its similarity scores with other movies, sorts them, and displays the top 5 recommendations.

I also integrated the TMDB API to fetch and display posters for the recommended movies.

🛠️ Technologies Used

- Python – Programming
- Pandas – Data processing
- Scikit-learn – Machine Learning & Cosine Similarity
- Streamlit – Web application and UI
- Requests – API requests
- TMDB API – Movie posters
- Git & GitHub – Version control
- Streamlit Community Cloud – Deployment

✨ Features

- 🎥 Select movies from the dataset
- 🤖 Get top 5 similar movies
- 🧠 Content-based recommendation
- 🖼️ Display movie posters
- 🎨 Netflix-inspired dark UI
- 🌐 Live deployed application

📂 Project Files

- "app.py" – Main Streamlit application and recommendation logic
- "movies.pkl" – Processed movie data
- "similarity.pkl" – Precomputed similarity matrix
- "requirements.txt" – Required Python libraries
- ".gitignore" – Files excluded from GitHub

 Author

Tejaswi
