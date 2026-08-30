from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_NAME = "facebook/bart-large-cnn"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

text = """
Artificial intelligence has become an important technology in modern
healthcare. Machine learning models can analyze medical images, assist
doctors with diagnosis, and help researchers discover new treatments.
However, these systems require large amounts of high-quality data and
must be carefully evaluated before being used in clinical settings.
"""

inputs = tokenizer(
    text,
    return_tensors="pt",
    truncation=True,
    max_length=1024
)

summary_ids = model.generate(
    inputs["input_ids"],
    max_length=100,
    min_length=30,
    num_beams=4,
    early_stopping=True
)

summary = tokenizer.decode(
    summary_ids[0],
    skip_special_tokens=True
)

print("SUMMARY:")
print(summary)