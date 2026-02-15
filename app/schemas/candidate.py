from pydantic import BaseModel, Field
from fastapi import Form
from typing import List
from datetime import date


# Response model
class CandidateResponse(BaseModel):
    id: int
    full_name: str
    dob: date
    contact_number: str
    contact_address: str
    education_qualification: str
    graduation_year: int
    years_of_experience: float
    skill_set: List[str]   # <-- LIST now
    resume_filename: str
    resume_path: str


# Input model for form
class CandidateCreate(BaseModel):
    full_name: str
    dob: date
    contact_number: str
    contact_address: str
    education_qualification: str
    graduation_year: int
    years_of_experience: float
    skill_set: str

    @classmethod
    def as_form(
        cls,
        full_name: str = Form(...),
        dob: date = Form(...),
        contact_number: str = Form(...),
        contact_address: str = Form(...),
        education_qualification: str = Form(...),
        graduation_year: int = Form(...),
        years_of_experience: float = Form(...),
        skill_set: str = Form(...),
    ):
        return cls(
            full_name=full_name,
            dob=dob,
            contact_number=contact_number,
            contact_address=contact_address,
            education_qualification=education_qualification,
            graduation_year=graduation_year,
            years_of_experience=years_of_experience,
            skill_set=skill_set,
        )
