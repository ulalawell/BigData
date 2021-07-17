import sys
import pandas as pd
import pyarrow.parquet as pq


def csv_to_parquet(csv_file, parquet_file, engine='auto', compression='snappy'):
    """
           Converts a csv file to a parquet file.
           You can choose different engines, compressions

           Parameters
           ----------
           csv_file : name of a csv file to convert
           parquet_file : name of a parquet file after conversion
           engine : {{'auto', 'pyarrow', 'fastparquet'}}, default 'auto'
           compression : {{'auto', 'gzip', 'brotli', None}}, default 'snappy'
    """
    try:
        data_frame = pd.read_csv(csv_file)
        data_frame.set_index(list(data_frame.columns), inplace=True)
        data_frame.to_parquet(parquet_file, engine=engine, compression=compression, index=None)
    except Exception:
        print(sys.exc_info()[1])


def parquet_to_csv(parquet_file, csv_file):
    """
           Converts a parquet file to a csv file.

           Parameters
           ----------
           parquet_file : name of a parquet file to convert
           csv_file : name of a csv file after conversion
    """
    try:
        data_frame = pd.read_parquet(parquet_file)
        data_frame.to_csv(csv_file)
    except Exception:
        print(sys.exc_info()[1])


def get_parquet_schema(parquet_file):
    """
           Returns the Parquet schema

           Parameters
           ----------
           parquet_file : name of a parquet file
    """
    try:
        parquet_file = pq.ParquetFile(parquet_file)
        return parquet_file.schema
    except Exception:
        print(sys.exc_info()[1])
