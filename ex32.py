from google import genai

# Replace with your Gemini API Key
client = genai.Client(api_key=" ")

prompts = {

    "Prompt 1": """
Write about Artificial Intelligence.
""",

    "Prompt 2": """
Write a short paragraph about Artificial Intelligence.
Include its definition, advantages, and applications.
""",

    "Prompt 3": """
You are an AI expert.

Write a 150-word paragraph explaining Artificial Intelligence.

Include:
1. Definition
2. Applications
3. Advantages
4. Future Scope

Use simple English.
Return only the paragraph.
"""
}

for name, prompt in prompts.items():

    print("="*60)
    print(name)
    print("="*60)

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    print(response.text)
    print("\n")
