# ai-text-summarizer

A small FastAPI service that summarizes PDF documents. Upload a PDF, and it extracts the text, cleans it, splits it into model-sized chunks, summarizes each chunk with BART, then produces a final combined summary.

## How it works

1. **Extract** — `src/pdf_reader.py` pulls raw text out of the uploaded PDF page by page (via `pypdf`).
2. **Clean** — `src/preprocessing.py` collapses extra whitespace/newlines and tidies up punctuation spacing.
3. **Chunk** — `src/chunking.py` tokenizes the cleaned text and splits it into chunks that fit within the model's max input length.
4. **Summarize** — `src/summarizer.py` runs each chunk through `facebook/bart-large-cnn`, then summarizes the concatenation of those chunk-summaries to produce one final summary.

## Requirements

- Python 3.10+
- See `requirements.txt` for pinned dependencies (FastAPI, Transformers, PyTorch (CPU), pypdf, etc.)

## Setup

```bash
pip install -r requirements.txt
```

## Running the API

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Endpoint

**POST** `/summarize`

Upload a PDF as multipart form-data under the field `file`:

```bash
curl -X POST http://localhost:8000/summarize \
  -F "file=@/path/to/document.pdf"
```

**Response:**

```json
{
  "summary": "..."
}
```

## Running with Docker

```bash
docker build -t ai-text-summarizer .
docker run -p 8000:8000 ai-text-summarizer
```

## Notes

- The BART model (`facebook/bart-large-cnn`) is downloaded from Hugging Face on first run and loaded into memory at import time, so the first request (and first startup) will be slow.
- `src/pdf_reader.py` can also be run directly (`python src/pdf_reader.py`) against a local file at `data/sample.pdf` for quick debugging outside the API — it prints extraction/chunking/summary stats to the console.

## License

This project is licensed under the MIT License.