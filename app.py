from flask import Flask, redirect, render_template, request
from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

movie_repository = get_movie_repository()
movies = {}


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    return render_template('list_all_movies.html', list_movies_active=True)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    
    # TODO: Feature 2
    title = request.form.get('movieTitle', type = str)
    director = request.form.get('director', type = str)
    rating = request.form['rating']
    
    for i in range(1):
        key = title
        movies.setdefault(key, [])
        movies[key].append(director,rating)
    # After creating the movie in the database, we redirect to the list all movies page
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    return render_template('search_movies.html', search_active=True)
