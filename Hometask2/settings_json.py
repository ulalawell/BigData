import csv
import json
from logger import get_module_logger

logger = get_module_logger(__name__)


def set_configuration_json(movies_file_name="data/movies.csv", ratings_file_name="data/ratings.csv", delimiter=","):
    """
                Writes such configuration settings, as 'Output file delimiter'
                                                        'Header line movies'
                                                        'Header line ratings'
                                                        'Header line output'
                in json file

                Parameters
                ----------
                movies_file_name: a csv file which contains info with this structure: movieId,title,genres
                ratings_file_name: file which contains info with this structure: userId,movieId,rating,timestamp
                delimiter: delimiter in output
    """
    try:
        with open(movies_file_name, 'r') as movies_csv:
            csv_reader = csv.reader(movies_csv)
            header_line_movies = next(csv_reader)
        with open(ratings_file_name, 'r') as movies_csv:
            csv_reader = csv.reader(movies_csv)
            header_line_ratings = next(csv_reader)
        header_line_output = '{1}{0}{2}{0}avg_rating'.format(delimiter, header_line_movies[2], header_line_movies[1])

        data = [
            {
                'Output file delimiter': delimiter,
                'Header line movies': header_line_movies,
                'Header line ratings': header_line_ratings,
                'Header line output': header_line_output,
            }]

        with open('data/configuration.json', "w") as f:
            json.dump(data, f, sort_keys=True)
    except OSError:
        logger.exception("check, please, filename argument")
    except TypeError:
        logger.exception("check, please, types of arguments")
