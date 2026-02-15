from fastapi import FastAPI

app = FastAPI(title='Mini Resume Collector Application')

@app.get('/health', tags=['Health'])
def health_check():
    return {"status": "OK", "message": "API is running"}