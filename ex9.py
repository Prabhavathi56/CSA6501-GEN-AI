from transformers import pipeline

# Load pre-trained GPT-2 model
generator = pipeline("text-generation", model="gpt2")

# Generate text
result = generator("Artificial Intelligence is", max_length=30)

print(result[0]["generated_text"])
