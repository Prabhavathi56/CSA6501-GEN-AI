import os
from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import pipeline

# ==========================================
# 1. ENTER PDF FILE PATH
# ==========================================

pdf_path = input("Enter PDF file path: ")

if not os.path.exists(pdf_path):
    print("PDF file not found!")
    exit()

# ==========================================
# 2. READ PDF
# ==========================================

reader = PdfReader(pdf_path)

text = ""

for page in reader.pages:
    text += page.extract_text() or ""

print("\nPDF loaded successfully.")
print("Pages:", len(reader.pages))

# ==========================================
# 3. SPLIT TEXT INTO CHUNKS
# ==========================================

words = text.split()

chunks = []

for i in range(0, len(words), 150):
    chunk = " ".join(words[i:i + 150])

    if chunk.strip():
        chunks.append(chunk)

print("Chunks created:", len(chunks))

# ==========================================
# 4. CREATE VECTOR DATABASE
# ==========================================

vectorizer = TfidfVectorizer()

vectors = vectorizer.fit_transform(chunks)

print("Vector database created.")

# ==========================================
# 5. LOAD LOCAL AI MODEL
# ==========================================

print("\nLoading local AI model...")
print("Please wait...")

qa_model = pipeline(
    "question-answering",
    model="distilbert-base-cased-distilled-squad"
)

print("AI model loaded successfully.")

# ==========================================
# 6. RAG FUNCTION
# ==========================================

def ask_question(question):

    # Convert question into vector
    question_vector = vectorizer.transform([question])

    # Find similarity
    similarity = cosine_similarity(
        question_vector,
        vectors
    )[0]

    # Find best matching chunk
    best_index = similarity.argmax()

    context = chunks[best_index]

    # Generate answer
    result = qa_model(
        question=question,
        context=context
    )

    print("\n--------------------------------")
    print("QUESTION:")
    print(question)

    print("\nANSWER:")
    print(result["answer"])

    print("\nSOURCE:")
    print(pdf_path)

    print("--------------------------------")


# ==========================================
# 7. ASK QUESTIONS
# ==========================================

while True:

    question = input(
        "\nEnter your technical question "
        "(type exit to stop): "
    )

    if question.lower() == "exit":
        print("\nProgram ended.")
        break

    if question.strip() == "":
        print("Please enter a question.")
        continue

    ask_question(question)
