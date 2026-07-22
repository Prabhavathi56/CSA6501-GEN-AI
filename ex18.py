from transformers import BertTokenizer, BertModel
import torch

# Load BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")

# Two similar sentences
sentence1 = "The cat is sitting on the mat."
sentence2 = "A cat is sitting on the mat."

# Tokenize
inputs1 = tokenizer(sentence1, return_tensors="pt")
inputs2 = tokenizer(sentence2, return_tensors="pt")

# Generate embeddings
with torch.no_grad():
    output1 = model(**inputs1)
    output2 = model(**inputs2)

# Get CLS embeddings
embedding1 = output1.last_hidden_state[:, 0, :]
embedding2 = output2.last_hidden_state[:, 0, :]

# Calculate cosine similarity
similarity = torch.nn.functional.cosine_similarity(embedding1, embedding2)

# Display results
print("Sentence 1:", sentence1)
print("Sentence 2:", sentence2)
print("Cosine Similarity:", similarity.item())
