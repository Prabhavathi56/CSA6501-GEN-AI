from google import genai

# Replace with your Gemini API Key
client = genai.Client(api_key=" ")

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="""
You are an SQL expert.

Database Schema:

Student(
    StudentID INT,
    Name VARCHAR(50),
    Department VARCHAR(30),
    Marks INT
)

Task:
Generate an SQL query to display the names and marks of students who scored more than 80 marks.

Requirements:
1. Return only the SQL query.
2. Do not include explanations.
3. Use standard SQL syntax.
"""
)

print("Generated SQL Query:\n")
print(response.text)
