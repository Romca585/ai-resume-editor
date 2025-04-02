from typing import Tuple
from pdfminer.high_level import extract_text
from docx import Document
from openai import OpenAI
import os

def parse_resume(file_path: str) -> Tuple[str, list[str]]:
    # For now, just pretend to extract a name and skills
    return ("Jane Doe", ["Python", "FastAPI", "React"])

def extract_resume_text(file_path: str) -> str:
    if file_path.endswith(".pdf"):
        return extract_text(file_path)
    elif file_path.endswith(".docx"):
        doc = Document(file_path)
        return "\n".join([p.text for p in doc.paragraphs])
    else:
        return ""
        
def parse_resume_with_gpt(resume_text: str) -> str:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    prompt = f"""
You are an AI that extracts structured info from a resume. Return JSON with:
- name
- email
- phone
- skills (as a list)
- work_experiences (as a list)
- extracurricular_experiences (as a list)
- educational_experiences (as a list)
- other_experiences (as a list) and this will include anything that is not strictly under any of the other experience categories

Resume text:
\"\"\"
{resume_text}
\"\"\"
"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{ "role": "user", "content": prompt }]
        )
        return response.choices[0].message.content
    except Exception as e:
        import traceback
        print("GPT API ERROR:")
        traceback.print_exc() #this will print the full error
        return '{"error": "GPT parsing failed"}'

def tailor_resume(gpt_resume_text: str, job_description: str) -> str:
    if not job_description.strip():
        print("No job description provided — skipping tailoring.")
        return gpt_resume_text
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    prompt = f"""
You're a professional resume editor. Take the following resume content and adjust it to better match the job description. Keep the original resume structure, but rephrase experience, skills, and summary sections to align with keywords and requirements from the job. Make sure to not lie about anything. If the user did not mention something in their resume, do not put it in.

Only rewrite the resume. Do not include explanations or extra text.

---
Resume:
{gpt_resume_text}

---
Job Description:
{job_description}

---
Edited Resume:

---
Main keywords found in description:
"""


    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )
        return response.choices[0].message.content
    except Exception as e:
        print("GPT Edit Error:", e)
        return "[Error tailoring resume]"


