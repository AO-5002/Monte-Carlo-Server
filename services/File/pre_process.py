from typing import NamedTuple
from fastapi import UploadFile
import pandas as pd
import numpy as np

# Main functions

# Define the schema for ParseResults
class ParseResult(NamedTuple):
    tickers: np.array
    portfolio_value: float
    portfolio_std: float

def parse_via_pandas(file: UploadFile) -> ParseResult:

    # Check whether it's a CSV or Excel file

    if file.filename.endswith('.csv'):
        df = pd.read_csv(file.file)

        tickers = df['Ticker'].to_numpy()
        shares = df['Portfolio_Shares'].to_numpy()
        portfolio_value = df['Portfolio_value'].to_numpy()





    else:
        raise Exception("File must be CSV or Excel")

    # Then, parse the data respectively





    # Returns x, y cols


    return df
