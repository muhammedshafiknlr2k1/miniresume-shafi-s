# Mini Resume Collector Application
A simple **FastAPI-based app** to collect candidate resumes, store metadata in memory, and provide filtering/search functionality.

---

## Folder Structure

- **app/** – Main application code  
  - **main.py** – FastAPI app instance, includes routes  
  - **routes/candidate_routes.py** – API endpoints for candidate operations  
  - **schemas/candidate.py** – Pydantic models for candidate data  
  - **services/candidate_service.py** – Business logic for candidates  
  - **utils/file_utils.py** – Functions to save uploaded resumes  
  - **utils/validators.py** – Input validation functions  

- **uploads/** – Auto-created folder to store uploaded resumes  
- **requirements.txt** – Python dependencies  
- **README.md** – Project documentation  

---
---
## Requirements
- **Python** - 3.10+
- **FastAPI** - Python Web framework for building APIs
- **uvicorn** - ASGI server to run FastAPI app
- **python-multipart** - Handle file uploads (Form + UploadFile)
---
---
##  Installation

Clone the repository:

```bash
git clone https://github.com/muhammedshafiknlr2k1/miniresume-shafi-s.git
```
Navigate into the project folder

```bash
cd miniresume-shafi-s
```
Create a virtual environment:

```bash
python -m venv name_of_the_venv
```
Activate the environment:

```bash
# Linux / Mac
source env_name/bin/activate

# Windows
env_name\Scripts\activate
```
Install dependencies:

```bash
pip install -r requirements.txt
```
---
---
## Running the App

Navigate into the app folder:
```bash
cd app
```
Start the FastAPI server
```bash
#By default app runs in port 8000 and --reload optional if we dont want to auto-reload the server after making changes

uvicorn main:app --reload
```
Open your browser to test:

- **Swagger UI(interactive testing):** - http://127.0.0.1:8000/docs

>The app runs on http://127.0.0.1:8000 by default.

---
---
## API Endpoints
| Method | Endpoint         | Description                                                                    |
| ------ | ---------------- | ------------------------------------------------------------------------------ |
| GET    | /health          | Check API status                                                               |
| POST   | /candidates      | Upload candidate resume and metadata                                           |
| GET    | /candidates      | List all candidates (optional filters: skill, min_experience, graduation_year) |
| GET    | /candidates/{id} | Get candidate by ID                                                            |
| DELETE | /candidates/{id} | Delete candidate by ID                                                         |

---
---
## Notes
- Uploaded resumes are stored in `uploads` automatically.  
- All data is **in-memory**, restarting the server clears all candidates.  
- Followed **PEP8 standards** and **professional FastAPI structure**
---
