import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from models.serializers import CorrectorRequest


DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
USE_HALF = True if DEVICE == "cuda" else False
MODEL_PATH = "ZurabDz/geo-spell-check-v8"
MAX_LENGTH = 64
TOP_K = 30
TOP_P = 0.95


model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH).to(DEVICE)
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, padding=True)
model.eval()


def inference(input: CorrectorRequest):
    input_ids = tokenizer(input.texts, return_tensors="pt", padding=True)["input_ids"]
    input_ids = input_ids.to(DEVICE)

    with torch.no_grad():
        outputs = model.generate(
            input_ids,
            max_length=MAX_LENGTH,
            do_sample=True,
            top_k=TOP_K,
            top_p=TOP_P,
            pad_token_id=model.config.pad_token_id,
        )

    # Decode output
    output_text = tokenizer.batch_decode(outputs, skip_special_tokens=True)
    return output_text
