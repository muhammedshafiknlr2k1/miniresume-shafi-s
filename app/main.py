from fastapi import FastAPI
from app.routes.candidate_routes import router as candidate_router


app = FastAPI(title='Mini Resume Collector Application')


#Include candidate routes
app.include_router(candidate_router)


#Health Check Endpoint
@app.get('/health', tags=['Health'])
def health_check():
    return {"status": "OK", "message": "API is running"}