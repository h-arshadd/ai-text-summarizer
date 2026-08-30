import re


def clean_text(text):
    # Replace multiple spaces/tabs with a single space
    text = re.sub(r"[ \t]+", " ", text)

    # Replace excessive newlines with a single newline
    text = re.sub(r"\n\s*\n+", "\n\n", text)

    # Remove spaces before punctuation
    text = re.sub(r"\s+([,.!?;:])", r"\1", text)

    return text.strip()