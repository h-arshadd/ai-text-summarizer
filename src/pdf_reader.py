from pypdf import PdfReader


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

    print(f"Number of characters: {len(text)}")
    print("\nFirst 2000 characters:\n")
    print(text[:2000])