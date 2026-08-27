import os
from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import pipeline

# ==========================================
# 1. ENGINEERING PDF PATH
# ==========================================

pdf_path = r"D:\gen ai\engineering.pdf"

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

print("Engineering document loaded.")
print("Number of pages:", len(reader.pages))

# ==========================================
# 3. SPLIT DOCUMENT INTO CHUNKS
# ==========================================

words = text.split()

chunks = []

for i in range(0, len(words), 150):
    chunk = " ".join(words[i:i + 150])

    if chunk.strip():
        chunks.append(chunk)

print("Chunks created:", len(chunks))

# ==========================================
# 4. CREATE LOCAL VECTOR DATABASE
# ==========================================

vectorizer = TfidfVectorizer()

vectors = vectorizer.fit_transform(chunks)

print("Vector database created.")

# ==========================================
# 5. LOAD LOCAL AI MODEL
# ==========================================

print("\nLoading AI model...")
print("Please wait...")

model = pipeline(
    "question-answering",
    model="distilbert-base-cased-distilled-squad"
)

print("AI model loaded.")

# ==========================================
# 6. RAG TROUBLESHOOTING
# ==========================================

def troubleshoot(problem):

    # Convert problem into vector
    problem_vector = vectorizer.transform([problem])

    # Calculate similarity
    similarity = cosine_similarity(
        problem_vector,
        vectors
    )[0]

    # Get top 3 relevant chunks
    top_indices = similarity.argsort()[-3:][::-1]

    print("\n====================================")
    print("RELEVANT ENGINEERING INFORMATION")
    print("====================================")

    for i, index in enumerate(top_indices):

        print("\nRelevant section", i + 1)
        print(chunks[index][:500])

    # Use the most relevant chunk
    best_index = top_indices[0]

    context = chunks[best_index]

    # Generate answer
    result = model(
        question=problem,
        context=context
    )

    print("\n====================================")
    print("TROUBLESHOOTING RECOMMENDATION")
    print("====================================")

    print("Problem:")
    print(problem)

    print("\nAnswer:")
    print(result["answer"])

    print("\nSource:")
    print(pdf_path)


# ==========================================
# 7. MAIN PROGRAM
# ==========================================

while True:

    problem = input(
        "\nEnter engineering problem "
        "(type exit to stop): "
    )

    if problem.lower() == "exit":
        print("Program ended.")
        break

    if problem.strip() == "":
        print("Please enter a problem.")
        continue

    troubleshoot(problem)
