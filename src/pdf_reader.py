from pypdf import PdfReader
from preprocessing import clean_text
from chunking import chunk_text
from summarizer import summarize_chunks


def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


if __name__ == "__main__":
    pdf_path = "data/sample.pdf"

    text = extract_text_from_pdf(pdf_path)
    cleaned_text = clean_text(text)

    print(f"Extracted characters: {len(text)}")
    print(f"Cleaned characters: {len(cleaned_text)}")

    chunks = chunk_text(cleaned_text)

    print(f"Number of chunks: {len(chunks)}")

    for i, chunk in enumerate(chunks):
        print(f"Chunk {i + 1}: {len(chunk)} characters")

    print("\nGenerating summaries...\n")

    summaries = summarize_chunks(chunks)

    for i, summary in enumerate(summaries):
        print(f"SUMMARY {i + 1}:")
        print(summary)
        print()