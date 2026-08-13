"""Verify BertViz demo dependencies and model load."""
from transformers import AutoTokenizer, AutoModel, utils

utils.logging.set_verbosity_error()

MODEL_NAME = "bert-base-uncased"
SENTENCE = "The cat sat on the mat because it was tired."

print("Loading tokenizer and model (first run downloads weights)...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModel.from_pretrained(MODEL_NAME, output_attentions=True)

inputs = tokenizer(SENTENCE, return_tensors="pt")
outputs = model(**inputs)
tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])

print("\nTokens:", tokens)
print("Layers:", len(outputs.attentions))
print("Attention shape (layer 0):", tuple(outputs.attentions[0].shape))
print("\nSetup OK — open bertviz_demo.ipynb and run all cells.")
