from google import genai

# Replace with your Gemini API Key
client = genai.Client(api_key=" ")

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Explain Artificial Intelligence in simple words."
)

print("Generated Response:\n")
print(response.text)
