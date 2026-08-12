# DOCUMENT QUESTION ANSWERING USING RAG

from google import genai
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ----------------------------------------
# API KEY
# ----------------------------------------

API_KEY = ""

client = genai.Client(api_key=API_KEY)

# ----------------------------------------
# DOCUMENT
# ----------------------------------------

chunks = [
    "Artificial Intelligence is a branch of computer science that creates systems capable of performing tasks that normally require human intelligence.",

    "Machine Learning is a subset of Artificial Intelligence. It allows computers to learn patterns from data without being explicitly programmed.",

    "Deep Learning is a subset of Machine Learning that uses artificial neural networks with multiple layers.",

    "Natural Language Processing enables computers to understand, process and generate human language.",

    "Generative AI can create new content such as text, images, audio, video and code."
]

# ----------------------------------------
# CREATE DOCUMENT VECTORS
# ----------------------------------------

vectorizer = TfidfVectorizer()

document_vectors = vectorizer.fit_transform(chunks)

# ----------------------------------------
# USER QUESTION
# ----------------------------------------

question = input("Ask a question about the document: ")

# ----------------------------------------
# CREATE QUESTION VECTOR
# ----------------------------------------

question_vector = vectorizer.transform([question])

# ----------------------------------------
# SIMILARITY SEARCH
# ----------------------------------------

scores = cosine_similarity(
    question_vector,
    document_vectors
)[0]

# Get top 2 chunks
top_k = 2

top_indices = scores.argsort()[-top_k:][::-1]

retrieved_chunks = []

for i in top_indices:
    retrieved_chunks.append(chunks[i])

# ----------------------------------------
# CREATE CONTEXT
# ----------------------------------------

context = "\n\n".join(retrieved_chunks)

# ----------------------------------------
# GENERATE ANSWER
# ----------------------------------------

prompt = f"""
You are a document question-answering system.

Use ONLY the information in the context below.

If the answer is not available in the context,
say: Answer not found in the document.

CONTEXT:
{context}

QUESTION:
{question}

Give a short and clear answer.
"""

try:

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    print("\n----------------------------")
    print("RETRIEVED CONTEXT")
    print("----------------------------")
    print(context)

    print("\n----------------------------")
    print("ANSWER")
    print("----------------------------")
    print(response.text)

except Exception as e:

    print("\nGemini API Error:")
    print(e)
