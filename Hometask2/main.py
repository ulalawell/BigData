from working_with_arguments import arguments
import operator
from parsing_data import processing_tools
import settings_json

if __name__ == '__main__':
    """
           main module, where a program starts
    """

    n, genres, year_from, year_to, regexp, delimiter, asc, gt, lt = arguments.get_arguments("data/movies.csv")
    settings_json.set_configuration_json("data/movies.csv", "data/ratings.csv", delimiter)
    genres = set(genres.split("|"))
    movies_dict = processing_tools.get_movies_dict(genres, year_from, year_to, regexp, "data/movies.csv")
    ratings_dict = processing_tools.get_ratings_dict(movies_dict, "data/ratings.csv")
    sorted_ratings = sorted(ratings_dict.items(), key=operator.itemgetter(1), reverse=not asc)
    processing_tools.print_movies(movies_dict, sorted_ratings, n, delimiter, gt, lt)
