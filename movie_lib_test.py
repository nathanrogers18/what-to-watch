from movie_lib import Movie, User, Rating, MovieLib
from nose.tools import raises

MOVIE_LIB = MovieLib()
TEST_MOVIE_LIB = MovieLib('ml-100k/utest.user', 'ml-100k/utest.item',
                          'ml-100k/utest.data')

def test_get_ratings_for_movie_by_id():
    """Find all ratings for a movie by id"""
    assert TEST_MOVIE_LIB.get_rating_numbers_for_movie(1) == [5, 5, 5, 5]

def test_get_average_rating_for_movie_by_id():
    """Find the average rating for a movie by id"""
    pass

def test_get_name_of_movie_by_id():
    """Find the name of a movie by id"""
    assert MOVIE_LIB.get_movie_name_by_id(1) == 'Toy Story (1995)'
    assert TEST_MOVIE_LIB.get_movie_name_by_id(1) == 'Toy Story (1995)'

def test_get_suggested_movies():
    """Show the top X movies by average rating with their rating."""
    assert TEST_MOVIE_LIB.get_suggested_movies(2) == [['Toy Story (1995)', 5.0],
                                                ['GoldenEye (1995)', 4.25]]

def test_get_suggested_movies_for_user():
    """Show the top X movies by average rating with their rating."""
    assert TEST_MOVIE_LIB.get_suggested_movies_for_user(2, 1) == [['Toy Story (1995)', 5.0],
                                                ['GoldenEye (1995)', 4.25]]


"""
The easiest way to recommend movies is to recommend the most popular movies.
Write a program to show the top X movies by average rating with their rating.
You need to be able to state a minimum number of ratings for a movie to be considered.

Now, create the ability to find the top X movies by average rating that a specific user has not rated.
This allows you to suggest popular movies for a specific user.
"""
