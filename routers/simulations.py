from fastapi import APIRouter, UploadFile, HTTPException
from services.File.validate import validate_file
from services.File.pre_process import parse_via_pandas

router = APIRouter()

@router.post("/upload")
async def run_var_simulation(file: UploadFile):

    # Validate the file type as CSV/Excel

    if(validate_file(file)):

        # Extract the tickers, portfolio value, and portfolio standard deviation

        tickers_list, portfolio_value, portfolio_std = parse_via_pandas(file)

        # Once we know what our tickers are, collect historical data on those tickers that spans
        # for 2 years via the Massive API




        return
    else:
        raise HTTPException(status_code=400, detail="File not valid")