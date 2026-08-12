# DOCUMENT STORAGE AND TOP-K RETRIEVAL USING FAISS

import faiss
from sklearn.feature_extraction.text import TfidfVectorizer

# -----------------------------
# 1. Documents
# -----------------------------

documents = [
    "Python is a popular programming language used in artificial intelligence.",
    "Machine learning allows computers to learn patterns from data.",
    "Deep learning uses neural networks to solve complex problems.",
    "Artificial intelligence enables machines to perform intelligent tasks.",
    "Natural language processing helps computers understand human language.",
    "Computer vision enables computers to understand images and videos.",
    "Football is a popular sport played around the world."
]

# -----------------------------
# 2. Convert documents to vectors
# -----------------------------

vectorizer = TfidfVectorizer()

document_vectors = vectorizer.fit_transform(documents)

# Convert to FAISS-compatible format
document_vectors = document_vectors.toarray().astype("float32")

# -----------------------------
# 3. Create FAISS vector database
# -----------------------------

dimension = document_vectors.shape[1]

index = faiss.IndexFlatL2(dimension)

# Store document vectors
index.add(document_vectors)

print("Vector database created successfully!")
print("Documents stored:", index.ntotal)

# -----------------------------
# 4. Get query
# -----------------------------

query = input("\nEnter your search query: ")

# Convert query into vector
query_vector = vectorizer.transform([query])
query_vector = query_vector.toarray().astype("float32")

# -----------------------------
# 5. Top-K retrieval
# -----------------------------

k = 3

distances, indices = index.search(query_vector, k)

# -----------------------------
# 6. Display results
# -----------------------------

print("\nTOP", k, "RETRIEVED DOCUMENTS")
print("==========================")

for i in range(k):

    document_index = indices[0][i]

    print("\nRank:", i + 1)
    print("Document:", documents[document_index])
    print("Distance:", round(float(distances[0][i]), 4))
