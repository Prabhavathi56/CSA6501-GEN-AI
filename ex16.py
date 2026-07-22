from transformers import BertTokenizer, GPT2Tokenizer

# Load tokenizers
bert_tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
gpt2_tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Input sentence
text = "Artificial Intelligence is transforming the world."

# Tokenize using BERT
bert_tokens = bert_tokenizer.tokenize(text)

# Tokenize using GPT-2
gpt2_tokens = gpt2_tokenizer.tokenize(text)

# Display results
print("Input Text:", text)

print("\nBERT Tokens:")
print(bert_tokens)

print("\nGPT-2 Tokens:")
print(gpt2_tokens)
