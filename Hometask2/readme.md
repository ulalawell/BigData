## Program structure
1) main.py -main module

2) settings_json.py - module, which sets configuration settings

3) logger.py - module, which returns logger with selected configs

4) working_with_arguments - directory, which contains

   >4.1)default_values.py - module, which gets defaults arguments 
   
   >4.2)arguments.py - module, which gets arguments


5) parsing_data - directory, which contains

   >5.1)processing_tools.py - module, with main functionality
   
   >5.2)restrictions.py - module, which checks restrictions on filters


6) data - directory with files

   >6.1)movies.csv - a csv file which contains info with this structure: `movieId`,`title`,`genres`
   
   >6.2)ratings.csv - a csv file which contains info with this structure: `userId`,`movieId`,`rating`,`timestamp`
   
   >6.3)info.log - log file
   
   >6.4)configuration.json -  a json file wich contains configuration settings with this structure:
   `Output file delimiter`
  `Header line movies`
   `Header line ratings`
    `Header line output`

## Usage


python3  main.py [-h] [-N MOVIES_NUMBER] [-genres MOVIES_GENRES] [-year_from YEAR_FROM] [-year_to YEAR_TO] 
[-regexp REGULAR_EXPRESSION] [-d DELIMITER] [-asc | -desc] [-gt GREATER_THEN] [-lt LOWER_THEN]

## Main task

To determine the top `N` most rated films (by average rating) for specified genres. The result will be a csv-like dataset with the `genre, title, rating`.


## Arguments description


| Option        | Description   |
| ------------- | ------------- |
| -h, --help  | show this help message and exit  |
|  -N MOVIES_NUMBER, --movies_number MOVIES_NUMBER  |   number of movies  |
|  -genres MOVIES_GENRES, --movies_genres MOVIES_GENRES  |  genres of movies, selected by user  |
|  -year_from YEAR_FROM, --year_from YEAR_FROM |    minimum year for movies |
|    -year_to YEAR_TO, --year_to YEAR_TO |    maximum year for movies |
|   -regexp REGULAR_EXPRESSION, --regular_expression REGULAR_EXPRESSION |  regular expression for movies title  |
|    -d DELIMITER, --delimiter DELIMITER|   delimiter in output |
|   -asc, --ascending|   keyword used to sort result in ascending order |
|  -desc, --descending|   keyword used to sort result in descending order|
|   -gt GREATER_THEN, --greater_then GREATER_THEN|   minimum average rating for a movie |
|  -lt LOWER_THEN, --lower_then LOWER_THEN|  maximum average rating for a movie|



## Examples

```bash
python3 main.py -genres "Action|Drama"  -year_from 2012 -year_to 2013 -lt 3.7 -gt 3.6 -asc
```
`genres,title,avg_rating`

{'Action'},Pacific Rim (2013),3.607142857142857

{'Drama'},Lawless (2012),3.625

{'Drama'},12 Years a Slave (2013),3.625

{'Drama', 'Action'},All Is Lost (2013),3.625

{'Drama'},Life of Pi (2012),3.629032258064516

{'Action'},The Hunger Games: Catching Fire (2013),3.6346153846153846

{'Action'},Looper (2012),3.640625

{'Drama'},Inside Llewyn Davis (2013),3.642857142857143

{'Drama'},Impossible, The (Imposible, Lo) (2012),3.6666666666666665

{'Action'},Star Trek Into Darkness (2013),3.685185185185185

{'Drama'},Saving Mr. Banks (2013),3.6875

```bash
python3 main.py  -N 3 -year_from 2017 -gt 4.8 -desc -d "|"
```
`genres|title|avg_rating`

{'Crime', 'Animation', 'Drama'}|Loving Vincent (2017)|5.0

{'Documentary'}|Tickling Giants (2017)|5.0

{'Documentary'}|Blue Planet II (2017)|5.0
```bash
python3 main.py  -year_from 2017 -year_to 2017  -gt 5.0  -desc -"Documentary"
```
`genres,title,avg_rating`

{'Documentary'},Tickling Giants (2017),5.0

{'Documentary'},Blue Planet II (2017),5.0

{'Documentary'},I Am Not Your Negro (2017),5.0



