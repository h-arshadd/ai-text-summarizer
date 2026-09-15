from fastapi import FastAPI, UploadFile, File

from src.pdf_reader import extract_text_from_pdf
from src.preprocessing import clean_text
from src.chunking import chunk_text
from src.summarizer import summarize_chunks, create_final_summary

app = FastAPI()


@app.post("/summarize")
def summarize(file: UploadFile = File(...)):
    text = extract_text_from_pdf(file.file)

    cleaned_text = clean_text(text)
    chunks = chunk_text(cleaned_text)
    summaries = summarize_chunks(chunks)
    final_summary = create_final_summary(summaries)

    return {"summary": final_summary}