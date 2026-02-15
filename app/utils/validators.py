import re
from datetime import date


ALLOWED_FILE_TYPES = [
    "application/pdf",
    "application/msword",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
]


#Validate Contact Number
def validate_contact_number(number: str):
    pattern = r"^\d{10}$"
    if not re.match(pattern, number):
        raise ValueError('Invalid contact number format')


#Validate year of Graduation
def validate_graduation_year(year: int):
    current_year = date.today().year
    if year < 1900 or year > (current_year + 5):
        raise ValueError('Year of Graduation is invalid')


#Validate Years of Experience
def validate_experience(years: float):
    if years < 0:
        raise ValueError('Years of experience cannot be negative')


#Validate Uploaded Resume Type
def validate_resume_file(content_type: str):
    if content_type not in ALLOWED_FILE_TYPES:
        raise ValueError('Resume file must be PDF, DOC, or DOCX')
