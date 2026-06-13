from flask import Flask, render_template, request
import sys
import os

# Add parent directory to path to import movie_recommender
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from movie_recommender.movie_recommender import recommend_movies

app = Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    movie_title = request.form.get('movie_title')
    recommendations = recommend_movies(movie_title, n=5)
    return render_template('index.html', recommendations=recommendations, input_title=movie_title)

# Vercel serverless handler
def handler(request):
    return app(request.environ, request.start_response)
