from google import genai

# Replace with your own Gemini API key
client = genai.Client(api_key=" ")

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Explain Artificial Intelligence in simple and easy words."
)

print(response.text)
