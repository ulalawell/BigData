import csv
import re
import sys
from logger import get_module_logger

logger = get_module_logger(__name__)


def get_max_movies_number(movies_file_name='data/movies.csv'):
    """
                Gets number of movies in a file

                Parameters
                ----------
                movies_file_name: a csv file which contains info with this structure: movieId,title,genres
    """
    try:
        line_counter = -1
        with open(movies_file_name) as file:
            for _ in file:
                line_counter += 1
            return line_counter

    except OSError:
        logger.exception("check, please, filename argument")


def get_all_movies_genres(movies_file_name='data/movies.csv'):
    """
                  Gets all genres of movies

                  Parameters
                  ----------
                  movies_file_name: a csv file which contains info with this structure: movieId,title,genres
    """
    try:
        s = set()
        with open(movies_file_name, 'r') as movies_csv:
            csv_reader = csv.reader(movies_csv)
            next(csv_reader)
            for movieId, title, movie_genres in csv_reader:
                for element in movie_genres.split("|"):
                    s.add(element)
            return "|".join(s)

    except OSError:
        logger.exception("check, please, filename argument")


def get_min_max_movies_year(movies_file_name='data/movies.csv'):
    """
                  Gets min and max years of movies in a file

                  Parameters
                  ----------
                  movies_file_name: a csv file which contains info with this structure: movieId,title,genres
      """
    try:
        min_year = sys.maxsize
        max_year = 0
        with open(movies_file_name, 'r') as movies_csv:
            csv_reader = csv.reader(movies_csv)
            for movieId, title, movie_genres in csv_reader:
                pattern = r"\(\d{4}\)"
                list_years = re.findall(pattern, title)
                if len(list_years) >= 1:
                    year = int(list_years[-1][1:5])
                    min_year = min(year, min_year)
                    max_year = max(year, max_year)
        return min_year, max_year

    except OSError:
        logger.exception("check, please, filename argument")


def get_min_max_movies_ratings(ratings_file_name='data/ratings.csv'):
    """
                 Gets min and max ratings of movies in a file

                  Parameters
                  ----------
                  ratings_file_name: a csv file which contains info with this structure: userId,movieId,rating,timestamp
      """
    try:
        min_rating = sys.maxsize
        max_rating = 0
        with open(ratings_file_name, 'r') as ratings_csv:
            csv_reader = csv.reader(ratings_csv)
            next(csv_reader)
            for userId, movieId, rating, timestamp in csv_reader:
                min_rating = min(float(rating), min_rating)
                max_rating = max(float(rating), max_rating)
        return min_rating, max_rating

    except OSError:
        logger.exception("check, please, filename argument")
