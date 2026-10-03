from services.ai_service import generate_questions

print("=== AI Interview Coach ===")

job_description = input("Paste the job description: ")

print("\nJob description received:")
print(job_description)

prompt = f"""
You are an AI interview coach.

The candidate is applying for the following position:

{job_description}

Generate 5 interview questions that are relevant to this position.
"""

print("\nPrompt sent to AI:")
print(prompt)

def generate_questions(job_description):
    job_description = job_description.lower()

    if "developer" in job_description:
        questions = [
            "Tell me about yourself.",
            "What programming languages are you most comfortable with?",
            "Tell me about a technical problem you have solved.",
            "How do you approach debugging?",
            "Why are you interested in this developer position?"
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

interview_questions = generate_questions(job_description)

print("\n=== Interview Questions ===")

for question in interview_questions:
    print(question)
    