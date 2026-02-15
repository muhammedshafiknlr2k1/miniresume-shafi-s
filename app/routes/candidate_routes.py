from fastapi import APIRouter, Form, UploadFile, Query, status, Depends, File
from typing import List, Optional
from datetime import date
from app.schemas.candidate import CandidateResponse, CandidateCreate
from app.services.candidate_service import (
    create_candidate_service,
    list_candidates_service,
    get_candidate_service,
    delete_candidate_service
)


router = APIRouter(prefix='/candidates', tags=['Candidates'])


#Create candidate endpoint
@router.post('', response_model=CandidateResponse, status_code=status.HTTP_201_CREATED)
def create_candidate(
    full_name: str = Form(...),
    dob: date = Form(...),
    contact_number: str = Form(...),
    contact_address: str = Form(...),
    education_qualification: str = Form(...),
    graduation_year: int = Form(...),
    years_of_experience: float = Form(...),
    skill_set: str = Form(...),
    resume_file: UploadFile = File(...)
):
    candidate = CandidateCreate(
        full_name=full_name,
        dob=dob,
        contact_number=contact_number,
        contact_address=contact_address,
        education_qualification=education_qualification,
        graduation_year=graduation_year,
        years_of_experience=years_of_experience,
        skill_set=skill_set
    )
    return create_candidate_service(candidate, resume_file)


#List Candidates Endpoint
@router.get("", response_model=List[CandidateResponse])
def list_candidates(
    skill: Optional[str] = Query(None),
    min_experience: Optional[float] = Query(None),
    graduation_year: Optional[int] = Query(None)
):
    return list_candidates_service(skill, min_experience, graduation_year)


#Get Candidate By Id
@router.get("/{candidate_id}", response_model=CandidateResponse)
def get_candidate(candidate_id: int):
    return get_candidate_service(candidate_id)


#Delete Candidate
@router.delete("/{candidate_id}")
async def delete_candidate(candidate_id: int):
    return delete_candidate_service(candidate_id)
