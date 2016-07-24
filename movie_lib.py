"""Movie Lib"""

import csv
import math
import statistics

def euclidean_distance(v, w):
    """Given two lists, give the Euclidean distance between them on a scale
    of 0 to 1. 1 means the two lists are identical.
    """

    # Guard against empty lists.
    if len(v) is 0:
        return 0

    # Note that this is the same as vector subtraction.
    differences = [v[idx] - w[idx] for idx in range(len(v))]
    squares = [diff ** 2 for diff in differences]
    sum_of_squares = sum(squares)

    return 1 / (1 + math.sqrt(sum_of_squares))

class Movie:
    """Movie Class"""
    def __init__(self, **kwargs):
        self.movie_id = int(kwargs['movie_id'])
        self.movie_title = kwargs['movie_title']
        self.release_date = kwargs['release_date']
        self.video_release_date = kwargs['video_release_date']
        self.imdb_url = kwargs['imdb_url']
        self.unknown = kwargs['unknown']
        self.action = kwargs['action']
        self.adventure = kwargs['adventure']
        self.animation = kwargs['animation']
        self.childrens = kwargs['childrens']
        self.comedy = kwargs['comedy']
        self.crime = kwargs['crime']
        self.documentary = kwargs['documentary']
        self.drama = kwargs['drama']
        self.fantasy = kwargs['fantasy']
        self.film_noir = kwargs['film_noir']
        self.horror = kwargs['horror']
        self.musical = kwargs['musical']
        self.mystery = kwargs['mystery']
        self.romance = kwargs['romance']
        self.sci_fi = kwargs['sci_fi']
        self.thriller = kwargs['thriller']
        self.war = kwargs['war']
        self.western = kwargs['western']

    def get_ratings_objects(self, rating_list=None):
        """Returns a list of rating objects for the movie.
           Optionally takes a ratings list created by MovieLib().ratings to
           improve performance. If not given, it will create this.
        """
        if rating_list:
            return [rating for rating in rating_list if self.movie_id == rating.item_id]
        else:
            return [rating for rating in MovieLib().ratings if self.movie_id == rating.item_id]


    def get_ratings_numbers(self, rating_list=None):
        """Returns a list of numeric ratings for the movie.
           Optionally takes a ratings list created by MovieLib().ratings to
           improve performance. If not given, it will create this.
        """
        if rating_list:
            return [rating.rating for rating in rating_list if self.movie_id == rating.item_id]
        else:
            return [rating.rating for rating in MovieLib().ratings if self.movie_id == rating.item_id]

    def get_average_rating(self, rating_list=None):
        """Returns the average numeric rating for the movie
           Optionally takes a ratings list created by MovieLib().ratings to
           improve performance. If not given, it will create this.
        """
        if rating_list: #TODO: add validation for empty ratings list
            return statistics.mean(self.get_ratings_numbers(rating_list))
        else:
            return statistics.mean(self.get_ratings_numbers())

    def __str__(self):
        return "ID: {} Title: {}".format(self.movie_id, self.movie_title)

class User:
    """User Class"""
    def __init__(self, **kwargs):
        self.user_id = int(kwargs['user_id'])
        self.age = kwargs['age']
        self.gender = kwargs['gender']
        self.occupation = kwargs['occupation']
        self.zip_code = kwargs['zip_code']

    def get_ratings_objects(self, rating_list=None):
        """Returns a list of numeric ratings for the user.
           Optionally takes a ratings list created by MovieLib().ratings to
           improve performance. If not given, it will create this.
        """
        if rating_list:
            return [rating for rating in rating_list if self.user_id == rating.user_id]
        else:
            return [rating for rating in MovieLib().ratings if self.user_id == rating.user_id]

    def get_ratings_numbers(self, rating_list=None):
        """Returns a list of numeric ratings for the user.
           Optionally takes a ratings list created by MovieLib().ratings to
           improve performance. If not given, it will create this.
        """
        if rating_list:
            return [rating.rating for rating in rating_list if self.user_id == rating.user_id]
        else:
            return [rating.rating for rating in MovieLib().ratings
                    if self.user_id == rating.user_id]

class Rating:
    """Rating Class"""
    def __init__(self, **kwargs):
        self.user_id = int(kwargs['user_id'])
        self.item_id = int(kwargs['item_id'])
        self.rating = float(kwargs['rating'])
        self.timestamp = kwargs['timestamp']




"""

u.data     -- The full u data set, 100000 ratings by 943 users on 1682 items.
              Each user has rated at least 20 movies.  Users and items are
              numbered consecutively from 1.  The data is randomly
              ordered. This is a tab separated list of
	         user id | item id | rating | timestamp.
              The time stamps are unix seconds since 1/1/1970 UTC

u.info     -- The number of users, items, and ratings in the u data set.

u.item     -- Information about the items (movies); this is a tab separated
              list of
              movie id | movie title | release date | video release date |
              IMDb URL | unknown | Action | Adventure | Animation |
              Children's | Comedy | Crime | Documentary | Drama | Fantasy |
              Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi |
              Thriller | War | Western |
              The last 19 fields are the genres, a 1 indicates the movie
              is of that genre, a 0 indicates it is not; movies can be in
              several genres at once.
              The movie ids are the ones used in the u.data data set.

u.genre    -- A list of the genres.

u.user     -- Demographic information about the users; this is a tab
              separated list of
              user id | age | gender | occupation | zip code
              The user ids are the ones used in the u.data data set.
"""

class MovieLib:
    """Creates the Movie Library Database"""
    def __init__(self,
                 users_file='ml-100k/u.user',
                 movies_file='ml-100k/u.item',
                 ratings_file='ml-100k/u.data'):
        self.users = []
        with open(users_file) as f:
            reader = csv.DictReader(f, delimiter='|',fieldnames=[
                'user_id', 'age', 'gender', 'occupation', 'zip_code'])
            for row in reader:
                self.users.append(User(**row))

        self.movies = {}
        with open(movies_file, encoding='latin_1') as f:
            reader = csv.DictReader(f, delimiter='|', fieldnames=[
                'movie_id', 'movie_title', 'release_date',
                'video_release_date', 'imdb_url', 'unknown', 'action',
                'adventure', 'animation', 'childrens', 'comedy', 'crime',
                'documentary', 'drama', 'fantasy', 'film_noir', 'horror',
                'musical', 'mystery', 'romance', 'sci_fi', 'thriller',
                'war', 'western'])
            for row in reader:
                self.movies[int(row['movie_id'])] = Movie(**row)

        self.ratings = []
        with open(ratings_file) as f:
            reader = csv.DictReader(f, delimiter='\t', fieldnames=[
                'user_id', 'item_id', 'rating', 'timestamp'])
            for row in reader:
                self.ratings.append(Rating(**row))

    def get_movie_name_by_id(self, movie_id):
        """Returns a movie name for a given movie id"""
        return self.movies[movie_id].movie_title

    def get_rating_objects_for_movie(self, movie_id):
        """Returns a list of rating objects for a given movie id."""
        return [rating for rating in self.ratings if rating.item_id == movie_id]

    def get_rating_numbers_for_movie(self, movie_id):
        """Returns a list of numeric ratings for the movie."""
        return [rating.rating for rating in self.ratings if rating.item_id == movie_id]

    def get_average_rating(self, movie_id):
        """Returns an average rating for a given movie id."""


    def get_ratings_objects_for_user(self, user_id):
        """Returns a list of rating objects for a given user id"""
        return [rating for rating in self.ratings if rating.user_id == user_id]

    def get_ratings_numeric_for_user(self, user_id):
        """Returns a list of numeric ratings for a given user id"""
        return [rating.rating for rating in self.ratings
                if rating.user_id == user_id]

    def get_suggested_movies(self, num_movies):
        """Returns top num_movies of movies by average rating.
        """
        average_ratings = [
            [self.movies[movie_id].movie_title,
             self.movies[movie_id].get_average_rating(self.ratings)]
            for movie_id in self.movies.keys()
        ]

        average_ratings.sort(key=lambda x: x[1], reverse=True)
        return average_ratings[:num_movies]

    def get_suggested_movies_for_user(self, num_movies, user_id):
        """Returns top num_movies of movies by average rating.
        """
        movies_watched = [rating.user_id for rating in self.ratings if user_id == rating.user_id]
        average_ratings = [
            [self.movies[movie_id].movie_title,
             self.movies[movie_id].get_average_rating(self.ratings)]
            for movie_id in self.movies.keys() if movie_id not in movies_watched]

        average_ratings.sort(key=lambda x: x[1], reverse=True)
        return average_ratings[:num_movies]

    def euc_distance(self, user_id_a, user_id_b):
        user_a_ratings = [[rating.item_id, rating.rating] for rating in self.ratings if rating.user_id == user_id_a]
        user_b_ratings = [[rating.item_id, rating.rating] for rating in self.ratings if rating.user_id == user_id_b]

        user_a_movies = [item[0] for item in user_a_ratings]
        user_b_movies = [item[0] for item in user_a_ratings]

        set(data1) & set(data2)



        user_a_ratings = [rate_list for rate_list in user_a_ratings if rate_list[0] in user_b_ratings]
        user_b_ratings = [rate_list for rate_list in user_b_ratings if rate_list[0] in user_a_ratings]

        user_a_ratings.sort(key=lambda x: x[0])
        user_a_ratings = [rating[1] for rating in user_a_ratings]
        print('user_a_ratings: ')
        print(user_a_ratings)

        user_b_ratings.sort(key=lambda x: x[0])
        user_b_ratings = [rating[1] for rating in user_b_ratings]
        print('user_b_ratings: ')
        print(user_b_ratings)

        return euclidean_distance(user_a_ratings, user_b_ratings)

def main():

    movie_lib = MovieLib()
    # #print(movie)
    # #print(movie.get_ratings())
    #
    # #top_movs = MovieLib().get_suggested_movies(10)
    # #print(top_movs)
    # #print(len(top_movs))
    #
    # toy_story = movie_lib.movies[1]
    # toy_story_rating_avg = toy_story.get_average_rating(movie_lib.ratings)
    #
    # toy_story_ratings = toy_story.get_ratings_numbers(movie_lib.ratings)
    # print(toy_story)
    #
    # print(toy_story_ratings)
    # print(toy_story_rating_avg)
    #

    TEST_MOVIE_LIB = MovieLib('ml-100k/utest.user', 'ml-100k/utest.item',
                               'ml-100k/utest.data')
    # print(TEST_MOVIE_LIB.get_rating_numbers_for_movie(1))
    # print(TEST_MOVIE_LIB.get_suggested_movies(2))
    # print(TEST_MOVIE_LIB.get_suggested_movies_for_user(3, 1))
    # print(TEST_MOVIE_LIB.get_suggested_movies(3))
    # print(TEST_MOVIE_LIB.get_rating_numbers_for_movie(1))

    #print(TEST_MOVIE_LIB.get_suggested_movies_for_user(6, 3))
    movie_lib.euc_distance(1,2)

if __name__ == '__main__':
    main()
