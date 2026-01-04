from typing import NamedTuple
from fastapi import UploadFile
import pandas as pd

# Main functions

# Define the schema for ParseResults
class ParseResult(NamedTuple):
    dataframe: pd.DataFrame
    file_size: int


def parse_via_pandas(file: UploadFile) -> ParseResult:

    # Check whether it's a CSV or Excel file

    if file.filename.endswith('.csv'):
        df = pd.read_csv(file.file)
    elif file.filename.endswith(('.xlsx', '.xls')):
        df = pd.read_excel(file.file)
    else:
        raise Exception("File must be CSV or Excel")

    # Then, parse the data respectively





    # Returns x, y cols


    return df



def parse_via_pyspark(file: UploadFile) -> ParseResult:
    return


def parse_data(file: UploadFile, FILE_SIZE: int, FILE_THRESHOLD: int) -> ParseResult:
    if(FILE_SIZE < FILE_THRESHOLD):
        return parse_via_pandas(file)
    else:
        return parse_via_pyspark(file)