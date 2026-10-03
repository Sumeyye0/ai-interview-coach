import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

USE_FAKE_AI = os.getenv("USE_FAKE_AI", "true").lower() == "true"


def generate_fake_questions(job_description):
    job_description = job_description.lower()

    if "developer" in job_description:
        questions = [
            "Tell me about yourself.",
            "What programming languages are you most comfortable with?",
            "Tell me about a technical problem you have solved.",
            "How do you approach debugging?",
            "Why are you interested in this developer position?"
        ]

    elif "hr" in job_description:
        questions = [
            "Tell me about yourself.",
            "How would you handle a conflict between two employees?",
            "What do you think makes a good workplace culture?",
            "How would you handle a difficult employee conversation?",
            "Why are you interested in working in HR?"
        ]

    elif "data" in job_description:
        questions = [
            "Tell me about yourself.",
            "What experience do you have with SQL?",
            "How would you analyze a large dataset?",
            "How do you communicate your findings to non-technical colleagues?",
            "Why are you interested in working with data?"
        ]

    else:
        questions = [
            "Tell me about yourself.",
            "Why are you interested in this position?",
            "What are your greatest strengths?",
            "Tell me about a challenge you have handled.",
            "Why should we hire you?"
        ]

    return questions

def generate_ai_questions(job_description, resume, level):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    prompt = f"""
    You are an AI interview coach.

    Job description:
    {job_description}

    Candidate resume:
    {resume}

    Candidate level:
    {level}

    Generate 5 interview questions tailored to both the job description
    and the candidate's experience.

    Adjust the difficulty based on the candidate level.

    Return only the questions, one question per line.
    """
    response = client.responses.create(
        model="gpt-6-astra",
        input=prompt
    )

    return response.output_text


def generate_questions(job_description, resume, level):
    if USE_FAKE_AI:
        return generate_fake_questions(job_description)

    return generate_ai_questions(job_description, resume, level)