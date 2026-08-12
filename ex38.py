# END-TO-END RAG PIPELINE
# Document Loading -> Chunking -> Embeddings -> Retrieval -> Generation

from google import genai
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ==========================================
# 1. GOOGLE GEMINI API KEY
# ==========================================

API_KEY = ""

client = genai.Client(api_key=API_KEY)

# ==========================================
# 2. DOCUMENT LOADING
# ==========================================

document = """
Artificial Intelligence is a branch of computer science that focuses
on creating machines capable of performing tasks that normally require
human intelligence.

Machine Learning is a subset of Artificial Intelligence. It allows
computers to learn patterns from data without being explicitly
programmed for every task.

Deep Learning is a subset of Machine Learning. It uses artificial
neural networks with multiple layers to learn complex patterns.

Natural Language Processing is a branch of Artificial Intelligence
that enables computers to understand and process human language.

Generative AI is a type of artificial intelligence that can generate
new content such as text, images, audio, video and code.
"""

print("Document loaded successfully.")

# ==========================================
# 3. TEXT CHUNKING
# ==========================================

chunks = [
    "Artificial Intelligence is a branch of computer science that focuses on creating machines capable of performing tasks that normally require human intelligence.",

    "Machine Learning is a subset of Artificial Intelligence. It allows computers to learn patterns from data without being explicitly programmed for every task.",

    "Deep Learning is a subset of Machine Learning. It uses artificial neural networks with multiple layers to learn complex patterns.",

    "Natural Language Processing is a branch of Artificial Intelligence that enables computers to understand and process human language.",

    "Generative AI is a type of artificial intelligence that can generate new content such as text, images, audio, video and code."
]

print("Text chunking completed.")
print("Number of chunks:", len(chunks))

# ==========================================
# 4. CREATE EMBEDDINGS
# ==========================================

vectorizer = TfidfVectorizer()

document_embeddings = vectorizer.fit_transform(chunks)

print("Embeddings generated successfully.")

# ==========================================
# 5. USER QUESTION
# ==========================================

question = input("\nEnter your question: ")

# ==========================================
# 6. QUERY EMBEDDING
# ==========================================

query_embedding = vectorizer.transform([question])

# ==========================================
# 7. RETRIEVAL
# ==========================================

similarities = cosine_similarity(
    query_embedding,
    document_embeddings
)[0]

# Retrieve top 2 chunks
top_k = 2

top_indices = similarities.argsort()[-top_k:][::-1]

retrieved_chunks = []

for index in top_indices:
    retrieved_chunks.append(chunks[index])

context = "\n\n".join(retrieved_chunks)

print("\nRelevant information retrieved successfully.")

# ==========================================
# 8. AUGMENTATION
# ==========================================

prompt = f"""
You are a document question-answering assistant.

Answer the question using ONLY the information provided
in the context.

If the answer is not present in the context, say:
"Answer not found in the document."

CONTEXT:
{context}

QUESTION:
{question}

Give a short and clear answer.
"""

# ==========================================
# 9. ANSWER GENERATION
# ==========================================

try:

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    print("\n===================================")
    print("RAG PIPELINE RESULT")
    print("===================================")

    print("\nRetrieved Context:")
    print(context)

    print("\nGenerated Answer:")
    print(response.text)

except Exception as e:

    print("\nGemini API Error:")
    print(e)
