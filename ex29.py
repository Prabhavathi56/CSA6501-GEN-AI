from google import genai

# Replace with your Gemini API Key
client = genai.Client(api_key=" ")

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="""
You are an expert Python programmer.

Generate a Python program to find the factorial of a number.

Requirements:
1. Use a function.
2. Take input from the user.
3. Print the factorial.
4. Add comments.
5. Return only Python code without explanation.
"""
)

print("Generated Python Code:\n")
print(response.text)
