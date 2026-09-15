from pypdf import PdfReader


def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


if __name__ == "__main__":
    from preprocessing import clean_text
    from chunking import chunk_text
    from summarizer import summarize_chunks, create_final_summary

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

    final_summary = create_final_summary(summaries)

    print("FINAL SUMMARY:")
    print(final_summary)