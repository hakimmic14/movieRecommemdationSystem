from flask import Flask, render_template, request
from movie_recommender.movie_recommender import recommend_movies

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    movie_title = request.form.get('movie_title')
    recommendations = recommend_movies(movie_title, n=5)
    
    error_message = None
    if not recommendations:
        error_message = f"Movie '{movie_title}' not found in our database. Try another movie!"
    
    return render_template('index.html', recommendations=recommendations, input_title=movie_title, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
