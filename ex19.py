from transformers import pipeline

# Load the pre-trained GPT-2 model
generator = pipeline("text-generation", model="gpt2")

# Input prompt
prompt = "Artificial Intelligence is"

# Generate text
result = generator(prompt, max_length=40, num_return_sequences=1)

# Display the generated text
print("Prompt:", prompt)
print("\nGenerated Text:")
print(result[0]["generated_text"])
