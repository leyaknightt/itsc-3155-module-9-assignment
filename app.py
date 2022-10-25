from flask import Flask, redirect, render_template, request

from src.repositories.movie_repository import get_movie_repository


app = Flask(__name__)

movie_repository = get_movie_repository()

# movie_repository.create_movie("black panther", "unknown", 10)
# movie_repository.create_movie("avengers", "unknown", 9)

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
    # After creating the movie in the database, we redirect to the list all movies page
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3

    movies = request.args.get('movies') 

    movie = movie_repository.get_movie_by_title(movies)


    return render_template('search_movies.html', search_active=True, movie=movie)
