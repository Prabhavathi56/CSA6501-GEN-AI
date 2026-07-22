from transformers import BertTokenizer, BertModel
import torch

# Load pre-trained BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")

# Input sentence
text = "Artificial Intelligence is transforming the world."

# Tokenize the input
inputs = tokenizer(text, return_tensors="pt")

# Generate contextual embeddings
with torch.no_grad():
    outputs = model(**inputs)

# Get the last hidden state (embeddings)
embeddings = outputs.last_hidden_state

print("Embeddings Shape:", embeddings.shape)
print(embeddings)
