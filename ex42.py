# MULTI-DOCUMENT AI ASSISTANT
# Supports multiple documents and question answering

from google import genai
import os


# ==========================================
# 1. GEMINI API KEY
# ==========================================

API_KEY = ""

client = genai.Client(api_key=API_KEY)


# ==========================================
# 2. UPLOAD / LOAD MULTIPLE DOCUMENTS
# ==========================================

documents = []

print("==========================================")
print("       MULTI-DOCUMENT AI ASSISTANT")
print("==================================

print("\nEnter the path of your text documents.")
print("Type DONE when you have added all documents.\n")


while True:

    file_path = input("Document path: ")

    if file_path.upper() == "DONE":
        break

    if os.path.exists(file_path):

        try:

            with open(file_path, "r", encoding="utf-8") as file:

                text = file.read()

            documents.append(text)

            print("Document loaded successfully.")

        except Exception as e:

            print("Could not read document:", e)

    else:

        print("File not found.")


# ==========================================
# 3. CHECK DOCUMENTS
# ==========================================

if len(documents) == 0:

    print("\nNo documents were loaded.")
    exit()

print("\nTotal documents loaded:", len(documents))


# ==========================================
# 4. COMBINE DOCUMENTS
# ==========================================

combined_documents = "\n\n".join(documents)


# ==========================================
# 5. QUESTION ANSWERING
# ==========================================

print("\n==========================================")
print("          QUESTION ANSWERING")
print("==========================================")

print("Ask questions about your documents.")
print("Type 'exit' to stop.")


while True:

    question = input("\nYou: ")

    if question.lower() == "exit":

        print("Assistant: Goodbye!")
        break


    # ======================================
    # 6. CREATE PROMPT
    # ======================================

    prompt = f"""
You are a document-based AI assistant.

Answer the user's question using ONLY the
information contained in the uploaded documents.

UPLOADED DOCUMENTS:
{combined_documents}

QUESTION:
{question}

Instructions:
1. Give a clear and simple answer.
2. Use information from the uploaded documents.
3. Do not invent information.
4. If the answer is not present, say:
   "Answer not found in the uploaded documents."
"""


    # ======================================
    # 7. GENERATE ANSWER
    # ======================================

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        print("\nAssistant:")
        print(response.text)

    except Exception as e:

        print("\nGemini API Error:")
        print(e)
