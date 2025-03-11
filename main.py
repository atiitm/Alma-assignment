from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel
from typing import Dict, List
from pypdf import PdfReader
from pypdf.errors import PdfReadError
import io
import spacy
from Criteria_rules import CRITERIA_RULES

app = FastAPI()

class AssessmentResult(BaseModel):
    criteria_matches: Dict[str, List[str]]
    rating: str

nlp = spacy.load("en_core_web_lg")

@app.get("/")
async def root():
    return {"message": "O-1A Visa Assessor - Use POST /assess endpoint"}

def extract_text(file):
    try:
        pdf = PdfReader(io.BytesIO(file))
        if not pdf.pages:
            raise HTTPException(400, "Empty PDF file")
        return "\n".join(page.extract_text() for page in pdf.pages)
    except PdfReadError:
        raise HTTPException(400, "Invalid PDF file") from None
    except Exception as e:
        raise HTTPException(400, f"PDF processing error: {str(e)}") from None

def analyze_criteria(text):
    doc = nlp(text.lower())
    results = {criterion: [] for criterion in CRITERIA_RULES}
    for criterion, keywords in CRITERIA_RULES.items():
        for keyword in keywords:
            if keyword in doc.text:
                results[criterion].append(keyword)
    return results

def calculate_rating(matches):
    score = sum(1 for v in matches.values() if v)
    if score >= 6:
        return "high"
    if score >= 3:
        return "medium"
    return "low"

def process_cv(text):
    matches = analyze_criteria(text)
    rating = calculate_rating(matches)
    return {"criteria_matches": matches, "rating": rating}

@app.post("/assess")
async def assess_cv(file: UploadFile = File(...)):
    if file.content_type not in ["application/pdf"]:
        raise HTTPException(400, "Unsupported file type. Only PDFs are accepted")
    try:
        contents = await file.read()
        text = extract_text(contents)
        return process_cv(text)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, f"Internal server error: {str(e)}")
