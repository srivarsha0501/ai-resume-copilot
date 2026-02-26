import requests


def generate_answer(question, context_chunks):
    context = "\n\n".join(context_chunks)

    prompt = f"""
You are a resume assistant.

Use the resume context below to answer.

Resume:
{context}

Question:
{question}
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi3",
                "prompt": prompt,
                "stream": False
            },
            timeout=300
        )

        if response.status_code != 200:
            return f"Ollama error: {response.text}"

        data = response.json()

        if "response" in data:
            return data["response"]

        return f"Ollama returned unexpected format:\n{data}"

    except Exception as e:
        return f"Error: {str(e)}"


def score_resume(resume_text):
    prompt = f"""
Evaluate this resume.

Return:
ATS Score (0-100)
Strengths
Missing skills
Improvements

Resume:
{resume_text}
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": "phi3",
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "stream": False
            },
            timeout=300
        )

        if response.status_code != 200:
            return response.text

        data = response.json()
        return data["message"]["content"]

    except Exception as e:
        return str(e)


def tailor_resume(resume_text, job_description):
    prompt = f"""
Rewrite this resume to better match the job description.

Rules:
- Keep truthful
- Improve wording
- Highlight relevant skills
- ATS friendly

JOB DESCRIPTION:
{job_description}

RESUME:
{resume_text}
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": "phi3",
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "stream": False
            },
            timeout=300
        )

        if response.status_code != 200:
            return response.text

        data = response.json()
        return data["message"]["content"]

    except Exception as e:
        return str(e)