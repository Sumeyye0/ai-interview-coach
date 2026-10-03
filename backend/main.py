from fastapi import FastAPI
from pydantic import BaseModel

from backend.services.ai_service import generate_questions

app = FastAPI(
    title="AI Interview Coach API",
    description="Backend API for generating role-specific interview questions.",
    version="0.1.0"
)


class InterviewRequest(BaseModel):
    job_description: str


@app.get("/")
def root():
    return {"message": "AI Interview Coach API is running"}


@app.post("/generate-questions")
def create_questions(request: InterviewRequest):
    questions = generate_questions(request.job_description)

    return {
        "questions": questions
    }