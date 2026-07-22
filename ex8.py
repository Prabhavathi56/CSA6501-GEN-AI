from transformers import BertTokenizer

# Load BERT Tokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

# Input text
text = "Artificial Intelligence is amazing."

# Tokenize the text
tokens = tokenizer.tokenize(text)

print("Original Text:", text)
print("Tokens:", tokens)
