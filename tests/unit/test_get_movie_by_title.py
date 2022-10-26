# TODO: Feature 3
from src.models.movie import Movie


def test_get_movie_by_title():
    movie = Movie('Star Wars', 'George Lucas', 5)
    assert movie.title == movie_repository.test_get_movie_by_title(Movie)

def test_get_movie_by_title_second():
    movie = Movie('Deadpool', 'Marvel', 5)

    assert type(movie) == Movie
    assert movie.title == 'Deadpool'
    assert movie.director == 'Marvel'
    assert movie.rating == 5