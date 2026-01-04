import os
from fastapi import UploadFile

def validate_file(file: UploadFile) -> bool:

    # Check if file fits a certain schema & is Excel/CSV

    _, ext = os.path.splitext(file.filename)
    allowed_extensions = {'.csv', '.xlsx', '.xls'}

    return ext.lower() in allowed_extensions
