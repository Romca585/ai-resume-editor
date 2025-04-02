from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.services.resume import parse_resume, extract_resume_text, parse_resume_with_gpt, tailor_resume

import os
import shutil

router = APIRouter()

UPLOAD_DIR = "uploaded_resumes"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload_resume")
async def upload_resume(file: UploadFile = File(...), job_description: str = Form("")):
    print("Upload hit!")
    if file.content_type not in ["application/pdf", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"]:
        raise HTTPException(status_code=400, detail="Only PDF and DOCX files are supported.")

    file_location = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    resume_text = extract_resume_text(file_location)
    gpt_parsed_json = parse_resume_with_gpt(resume_text)
    edited_resume = tailor_resume(gpt_parsed_json, job_description)

    return {
        "message": f"Resume uploaded as {file.filename}",
        "gpt_parsed": gpt_parsed_json,
        "edited_resume": edited_resume
    }
