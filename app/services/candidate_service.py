from fastapi import UploadFile, HTTPException, status
from typing import List, Optional
from datetime import date
from app.schemas.candidate import CandidateCreate, CandidateResponse
from app.utils import validators
from app.utils.file_utils import save_resume_file


# In-memory storage
candidates_db = {}
candidate_id_counter = 1


def create_candidate_service(
        candidate: CandidateCreate,
        resume_file: UploadFile
) -> CandidateResponse:
    global candidate_id_counter

    # validation
    try:
        validators.validate_contact_number(candidate.contact_number)
        validators.validate_graduation_year(candidate.graduation_year)
        validators.validate_experience(candidate.years_of_experience)
        validators.validate_resume_file(resume_file.content_type)
    except ValueError as ve:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(ve))

    resume_path = save_resume_file(resume_file)

    candidate_id = candidate_id_counter
    candidate_id_counter += 1
    skills_list = [s.strip() for s in candidate.skill_set.split(",")]
    candidate_dict = candidate.model_dump()
    candidate_dict['skill_set'] = skills_list
    candidate_dict.update({
        "id": candidate_id,
        "skill_set": skills_list,
        "resume_filename": resume_file.filename,
        "resume_path": resume_path
    })

    candidates_db[candidate_id] = candidate_dict

    return CandidateResponse(**candidate_dict)
