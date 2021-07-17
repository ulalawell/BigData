import sys
import converter
import os
import argparse


def validation_output_filename(input_file_name, output_file_name):
    """
           Validates output file name.
           If the output filename is empty, it discards the expansion from the input filename
           and changes it changes to the opposite one

           Parameters
           ----------
           input_file_name : name of a file to convert
           output_file_name : name of a file after conversion
    """
    try:
        if output_file_name == "":
            filename, file_extension = os.path.splitext(input_file_name)
            if file_extension == ".csv":
                output_file_name = filename + ".parquet"
            elif file_extension == ".parquet":
                output_file_name = filename + ".csv"
            else:
                output_file_name = filename + "_converted"
        return output_file_name
    except Exception:
        print(sys.exc_info()[1])


if __name__ == '__main__':

    """
           the module, which provides functionality to work with converter module
    """

    parser = argparse.ArgumentParser(description='converter for csv and parquet files')

    parser.add_argument('-in', '--input', type=str, required=True, help='name of file with expansion to convert')
    parser.add_argument('-out', '--output', type=str, required=False, default='',
                        help='name of file with expansion after conversion')
    parser.add_argument('-e', '--engine', type=str, required=False, default='auto', help='engine to use in conversion')
    parser.add_argument('-c', '--compression', type=str, required=False, default='snappy',
                        help='compression to use in conversion')

    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument('-to_prq', '--csv_to_parquet', action='store_true', help='converts a csv file to parquet')
    group.add_argument('-to_csv', '--parquet_to_csv', action='store_true', help='converts a parquet file to csv')
    group.add_argument('-schema', '--get_schema', action='store_true', help='gets schema of a parquet file')

    args = parser.parse_args()
    args.output = validation_output_filename(args.input, args.output)

    if args.csv_to_parquet:
        converter.csv_to_parquet(args.input, args.output, args.engine, args.compression)
    elif args.parquet_to_csv:
        converter.parquet_to_csv(args.input, args.output)
    elif args.get_schema:
        print(converter.get_parquet_schema(args.input))
