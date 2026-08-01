from google import genai

# Replace with your Gemini API Key
client = genai.Client(api_key=" ")

prompts = {
    "Zero-shot": """
Write a Python program to check whether a number is prime.
""",

    "One-shot": """
Example:

Input:
Find the factorial of a number

Output:
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

Now write a Python program to check whether a number is prime.
""",

    "Few-shot": """
Example 1:

Input:
Add two numbers

Output:
a = int(input())
b = int(input())
print(a+b)

Example 2:

Input:
Find factorial

Output:
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

Now write a Python program to check whether a number is prime.
"""
}

for prompt_type, prompt in prompts.items():

    print("="*50)
    print(prompt_type)
    print("="*50)

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    print(response.text)
