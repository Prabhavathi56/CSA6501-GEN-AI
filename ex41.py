from google import genai

# ==========================================
# GEMINI API KEY
# ==========================================

API_KEY = ""

client = genai.Client(api_key=API_KEY)


# ==========================================
# GET EXTERNAL DOCUMENT FROM USER
# ==========================================

print("======================================")
print("       AI DOCUMENT ASSISTANT")
print("======================================")

print("\nPaste your document text below.")
print("Type END on a new line when finished.\n")

lines = []

while True:
    line = input()

    if line == "END":
        break

    lines.append(line)

document = "\n".join(lines)


# ==========================================
# ASK QUESTIONS
# ==========================================

while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        print("Assistant: Goodbye!")
        break

    prompt = f"""
You are an AI assistant.

Answer the question using the external document
provided below.

EXTERNAL DOCUMENT:
{document}

QUESTION:
{question}

If the answer is not available in the document,
say:
"Answer not found in the document."

Give a simple and clear answer.
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        print("\nAssistant:", response.text)

    except Exception as e:

        print("\nError:", e)
