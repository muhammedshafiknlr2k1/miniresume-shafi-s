# Mini Resume Collector Application

A simple **FastAPI-based REST API** to collect candidate resumes, store metadata in memory, and provide filtering/search functionality.

---

## 📂 Folder Structure

miniresume-shafi-s/
│
├── app/                     # Main application code
│   ├── main.py              # Starts the FastAPI app and includes all routes
│   ├── routes/
│   │   └── candidate_routes.py  # API endpoints for candidate operations
│   ├── schemas/
│   │   └── candidate.py     # Pydantic models for candidate data
│   ├── services/
│   │   └── candidate_service.py  # Business logic for handling candidates
│   └── utils/
│       ├── file_utils.py    # Functions to save uploaded resumes
│       └── validators.py    # Input validation functions
│
├── uploads/        # Auto-created folder to store uploaded resumes
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation



**Note:** The `uploads` folder is **created automatically** when the first resume is uploaded, and all resume files are saved there.

---


## ⚙️ Installation

```bash
git clone https://github.com/yourusername/miniresume-shafi-s.git
cd miniresume-shafi-s
python -m venv venv
source venv/bin/activate      # Linux / Mac
venv\Scripts\activate         # Windows
pip install -r requirements.txt

Running the App
cd app
uvicorn main:app --reload


Swagger UI: http://127.0.0.1:8000/docs

ReDoc UI: http://127.0.0.1:8000/redoc

| Method | Endpoint         | Description                                                                    |
| ------ | ---------------- | ------------------------------------------------------------------------------ |
| GET    | /health          | Check API status                                                               |
| POST   | /candidates      | Upload candidate resume and metadata                                           |
| GET    | /candidates      | List all candidates (optional filters: skill, min_experience, graduation_year) |
| GET    | /candidates/{id} | Get candidate by ID                                                            |
| DELETE | /candidates/{id} | Delete candidate by ID                                                         |



