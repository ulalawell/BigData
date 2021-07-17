## Program structure
    
1) main.py -main module
   
2) converter.py - module, which contains converter
   
3) data - directory with files


# Dependences



```bash
pip install -r requirements.txt
```

## Usage

Program works with command line 

python3  main.py [-h] -in INPUT [-out OUTPUT] [-e ENGINE] [-c COMPRESSION] (-to_prq | -to_csv | -schema)


### Description 

-h, --help  
>shows help

-in INPUT_FILE,  --input INPUT_FILE 
>input file name

-out OUTPUT_FILE, --output OUTPUT_FILE  
>   output file name

-e ENGINE, --engine ENGINE 
> engine name

-c COMPRESSION, --compression COMPRESSION 
> compression name

-to_csv, --parquet_to_csv
> converts parquet file to csv file

-to_prq, --csv_to_parquet 
>converts csv file to parquet file

-schema, --get_schema 
>gets the schema of the parquet file

## Examples

```bash
python3 main.py -to_prq -in data/airtravel.csv -e pyarrow -c brotli -out data/airtravel.parquet
```
