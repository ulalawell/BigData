import argparse
from working_with_arguments import defaults_values


def get_arguments(movies_file_name="data/movies.csv", ratings_file_name="data/ratings.csv"):
    """
              gets arguments using argparse

              Parameters
              ----------
              movies_file_name: a csv file which contains info with this structure: movieId,title,genres
              ratings_file_name: a csv file which contains info with this structure: userId,movieId,rating,timestamp
    """

    max_movie_number = defaults_values.get_max_movies_number(movies_file_name)
    all_movies_genres = defaults_values.get_all_movies_genres(movies_file_name)
    min_year_movie, max_year_movie = defaults_values.get_min_max_movies_year(movies_file_name)
    min_rating_movie, max_rating_movie = defaults_values.get_min_max_movies_ratings(ratings_file_name)

    parser = argparse.ArgumentParser(description='program for finding movies')

    parser.add_argument('-N', '--movies_number', type=int, required=False, default=max_movie_number,
                        help='number of movies')
    parser.add_argument('-genres', '--movies_genres', type=str, required=False, default=all_movies_genres,
                        help='genres of movies, selected by user')
    parser.add_argument('-year_from', '--year_from', type=int, required=False, default=min_year_movie,
                        help='minimum year for movies')
    parser.add_argument('-year_to', '--year_to', type=int, required=False, default=max_year_movie,
                        help='maximum year for movies')
    parser.add_argument('-regexp', '--regular_expression', type=str, required=False, default=".+",
                        help='regular expression for movies title')
    parser.add_argument('-d', '--delimiter', type=str, required=False, default=",",
                        help='delimiter in output')

    group_order = parser.add_mutually_exclusive_group(required=False)
    group_order.add_argument('-asc', '--ascending', required=False, default=False, action='store_true',
                             help='keyword used to sort result in ascending order')
    group_order.add_argument('-desc', '--descending', required=False, default=False, action='store_true',
                             help='keyword used to sort result in descending order')

    parser.add_argument('-gt', '--greater_then', type=float, required=False, default=min_rating_movie,
                        help='minimum average rating for a movie')
    parser.add_argument('-lt', '--lower_then', type=float, required=False, default=max_rating_movie,
                        help='maximum average rating for a movie')

    args = parser.parse_args()

    return args.movies_number, args.movies_genres, args.year_from, \
           args.year_to, args.regular_expression, args.delimiter, \
           args.ascending, args.greater_then, args.lower_then
