from transformers import AutoTokenizer


MODEL_NAME = "facebook/bart-large-cnn"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)


def chunk_text(text):
    max_tokens = tokenizer.model_max_length - 50

    tokens = tokenizer.encode(text)

    chunks = []

    for start in range(0, len(tokens), max_tokens):
        token_chunk = tokens[start:start + max_tokens]

        chunk = tokenizer.decode(
            token_chunk,
            skip_special_tokens=True
        )

        chunks.append(chunk)

    return chunks