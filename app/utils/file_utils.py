from pathlib import Path
from fastapi import UploadFile, HTTPException, status

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)  

def save_resume_file(resume_file: UploadFile) -> str:
    """
    Save uploaded resume to 'uploads/' folder.
    Returns the file path.
    """
    file_path = UPLOAD_DIR / resume_file.filename
    try:
        contents = resume_file.file.read() 
        with open(file_path, "wb") as f:
            f.write(contents)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error saving resume: {str(e)}"
        )
    finally:
        resume_file.file.close()
    return str(file_path)
