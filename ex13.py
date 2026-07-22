from transformers import pipeline

# Load the pre-trained GPT-2 model
generator = pipeline("text-generation", model="gpt2")

# Input prompt
prompt = "Artificial Intelligence"

# Generate text
result = generator(prompt, max_length=30, num_return_sequences=1)

# Display the generated text
print("Generated Text:")
print(result[0]["generated_text"])
