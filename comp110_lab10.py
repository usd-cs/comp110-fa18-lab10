"""
Module: comp110_lab10

Modules with some functions for Lab 10 practice problems.
"""

import math

def read_movie_db(filename):
    """
    Reads data from a movie database file. Returns a dictionary that maps a
    movie id (an integer) to a (title, genre_list) tuple.
    """
    movie_dict = {}
    all_genres = []

    # Fill in body of the function here.

    return (movie_dict, all_genres)


def get_name(movie):
    """
    Returns the name of the movie parameter.
    """

    movie_name = "FIXME" # FIXME: replace "FIXME" with something from movie
    return movie_name


def get_genres(movie):
    """
    Returns the list of genres of the movie parameter.
    """

    movie_genres = []  # FIXME: replace [] with something from movie
    return movie_genres


def get_movies(movie_dict, target_genres):
    """
    Returns a list of movie names that has in its list of genres all genres in
    target_genres.
    """
    movie_names = []

    # Fill in body of the function here.

    return movie_names


# Do not modify the following code, except the name of the movies file to work
# with a smaller file.
if __name__ == "__main__":
    # Read in the movie database.
    (movie_dict, all_genres) = read_movie_db("movies.csv")

    # Print the genres
    print("  Genres:")
    for genre in all_genres:
        print(genre)
    print()

    # Print out the first ten movies
    print("   The first ten movies in the file")
    for i in range(1, 11):
        if i < len(movie_dict):
            print(movie_dict[i])
    print()


    # Get and print movies with action, comedy, and animation genres.
    movie_names = get_movies(movie_dict, ["Adventure", "Animation",
                                          "Children", "Comedy", "Fantasy",
                                          "IMAX"])
    print("   Movies with adventure, animation, children, comedy, fantasay, and IMAX genres")
    for movie_name in movie_names:
        print(movie_name)
