import re
from logger import get_module_logger

logger = get_module_logger(__name__)


def check_genres_restrictions(genres, movie_genres):
    """
              Checks if a movie contains genres, which user choose

              Parameters
              ----------
              genres: set of movies selected by user
              movie_genres: set of genres of movie
    """
    try:
        return len(genres & movie_genres) > 0
    except TypeError:
        logger.exception("check, please, types of arguments")


def check_year_restrictions(title, year_from=1895, year_to=2021):
    """
              Checks if the date of a movie respond to the year restrictions

              Parameters
              ----------
              title: title of a movie
              year_from: start year of movies for processing
              year_to: end year of movies for processing
    """
    try:
        pattern = r"\(\d{4}\)"
        years_list = re.findall(pattern, title)
        if len(years_list) >= 1:
            year = int(years_list[-1][1:5])
            return year_from <= year <= year_to
    except TypeError:
        logger.exception("check, please, types of arguments")


def check_regexp_restrictions(title, regexp=".+"):
    """
              Checks if the title of a movie respond to the regular expression

              Parameters
              ----------
              title: title of a movie
              regexp: pattern of regular expression
    """
    try:
        return re.search(regexp, title)
    except TypeError:
        logger.exception("check, please, types of arguments")


def check_rating_restrictions(avg_rating, lower_then, greater_then):
    """
              Checks if the average ratings is between [lower_then;greater_then]

              Parameters
              ----------
              avg_rating - an average rating
              lower_then -  maximum average rating for a movie
              greater_then -  minimum average rating for a movie
    """
    try:
        return greater_then <= avg_rating <= lower_then
    except TypeError:
        logger.exception("check, please, types of arguments")
