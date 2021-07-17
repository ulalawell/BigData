import csv
import json

from parsing_data import restrictions
import sys
from logger import get_module_logger

logger = get_module_logger(__name__)


def get_movies_dict(genres, year_from=1895, year_to=2021, regexp=".+", movies_file_name='data/movies.csv'):
    """
               Gets a dictionary from a csv file, where key = movieId and value=(title, genres)
               where movies respond to all restrictions

               Parameters
               ----------
               movies_file_name: a csv file which contains info with this structure: movieId,title,genres
               genres: set of movies selected by user
               year_from: start year of movies for processing
               year_to: end year of movies for processing
               regexp: pattern of regular expression
    """
    try:
        movies = dict()
        with open(movies_file_name, 'r') as movies_csv:
            csv_reader = csv.reader(movies_csv)
            next(csv_reader)
            for movieId, title, movie_genres in csv_reader:
                movie_genres = set(movie_genres.split("|"))
                if restrictions.check_genres_restrictions(genres, movie_genres) \
                        and restrictions.check_year_restrictions(title, year_from, year_to) \
                        and restrictions.check_regexp_restrictions(title, regexp):
                    movies[movieId] = (title, movie_genres & genres)
        return movies

    except MemoryError:
        logger.exception("there's no enough memory")
    except OSError:
        logger.exception("check, please, filename argument")
    except TypeError:
        logger.exception("check, please, types of arguments")


def get_ratings_dict(movies_dict, ratings_file_name='data/ratings.csv'):
    """
              Gets ratings of movies in movies dictionary

              Parameters
              ----------
              movies_dict: dictionary with this structure key = movieId and value=(title, genres)
                  ratings_file_name: a csv file which contains info with this structure: userId,movieId,rating,timestamp
    """
    try:
        ratings_dict = dict()
        with open(ratings_file_name, 'r') as ratings_csv:
            csv_reader = csv.reader(ratings_csv)
            next(csv_reader)
            for userId, movieId, rating, timestamp in csv_reader:
                if movieId in movies_dict.keys():
                    if movieId in ratings_dict.keys():
                        sum = ratings_dict[movieId][0]
                        amount = ratings_dict[movieId][1]
                        ratings_dict[movieId] = (sum + float(rating), amount + 1)
                    else:
                        ratings_dict[movieId] = (float(rating), 1)
        for key in ratings_dict:
            sum = ratings_dict[key][0]
            amount = ratings_dict[key][1]
            ratings_dict[key] = sum / amount
        return ratings_dict

    except OverflowError:
        logger.exception("overflow exception")
    except MemoryError:
        logger.exception("there's no enough memory")
    except OSError:
        logger.exception("check, please, filename argument")
    except TypeError:
        logger.exception("check, please, types of arguments")


def print_movies(movies_dict, sorted_ratings, n=sys.maxsize, delimiter=",", greater_then=0.0, lower_then=5.0):
    """
              Prints movies from movies_dict

              Parameters
              ----------
              movies_dict: dictionary with this structure key = movieId and value=(title, genres)
              sorted_ratings: list with this ratings
              n: number of films to print
              delimiter: delimiter in output
              lower_then:  maximum average rating for a movie
              greater_then:  minimum average rating for a movie
    """
    try:
        with open('data/configuration.json', 'r') as f:
            settings = json.loads(f.read())
            print(settings[0]["Header line output"])

        counter = 0
        index = 0
        while counter < n and index < len(sorted_ratings):
            genres = str(movies_dict[sorted_ratings[index][0]][1])
            title = movies_dict[sorted_ratings[index][0]][0]
            avg_rating = sorted_ratings[index][1]
            index += 1

            if restrictions.check_rating_restrictions(avg_rating, lower_then, greater_then):
                l = list()
                l.append(genres)
                l.append(title)
                l.append(str(avg_rating))
                print(delimiter.join(l))
                counter += 1


    except TypeError:
        logger.exception("check, please, types of arguments")
