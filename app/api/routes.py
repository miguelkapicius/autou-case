import io
from fastapi import APIRouter, File, Form, Request, UploadFile
from fastapi.templating import Jinja2Templates
from app.services.gemini import classify_text, suggest_reply
from app.core.npl import clean_text
import asyncio
from PyPDF2 import PdfReader

router = APIRouter(tags=["process"])
templates = Jinja2Templates(directory="app/templates")


@router.get("/health") 
async def health():
    return {"status": "OK"}

@router.get("/") 
async def form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@router.post("/process")
async def process(message: str = Form(...), file: UploadFile | None = File(None)):
    
    user_text = message
    
    if file:
        contents = await file.read()
        if file.filename.endswith(".txt"):
            user_text = contents.decode("utf-8")
        elif file.filename.endswith(".pdf"):
            reader = PdfReader(io.BytesIO(contents))
            user_text = ""
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    user_text +=page_text
        else:
            user_text = ""

    cleaned = clean_text(user_text)
    classification_task = asyncio.create_task(classify_text(cleaned))
    suggest_reply_task = asyncio.create_task(suggest_reply(cleaned))
    
    classification = await classification_task
    suggest_reply_text = await suggest_reply_task
    
    
    return {
        "classification": classification,
        "suggested_reply": suggest_reply_text
    }