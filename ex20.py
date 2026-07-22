from transformers import pipeline

# Load the pre-trained GPT-2 model
generator = pipeline("text-generation", model="gpt2")

# List of prompts
prompts = [
    "Artificial Intelligence is",
    "Machine Learning helps",
    "The future of technology"
]

# Generate text for each prompt
for prompt in prompts:
    result = generator(prompt, max_length=30, num_return_sequences=1)
    print("Prompt:", prompt)
    print("Generated Response:")
    print(result[0]["generated_text"])
    print("-" * 50)
