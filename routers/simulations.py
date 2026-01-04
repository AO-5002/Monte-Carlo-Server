from fastapi import APIRouter, UploadFile, HTTPException
from services.File.validate import validate_file

router = APIRouter()

# Size threshold: 100 MB
SIZE_THRESHOLD = 100 * 1024 * 1024  # bytes

@router.post("/upload")
async def run_var_simulation(file: UploadFile):

    # Validate the file type as CSV/Excel

    if(validate_file(file)):

        # Check the size & parse the data based on its size using Pandas or PySpark

        FILE_SIZE: int = file.size


        # Return the data from the simulation to visualize

    else:
        raise HTTPException(status_code=400, detail="File not valid")
