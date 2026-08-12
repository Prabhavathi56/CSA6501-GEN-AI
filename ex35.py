import faiss
from sklearn.feature_extraction.text import TfidfVectorizer

# Documents
documents = [
    "Python is a popular programming language.",
    "Machine learning allows computers to learn from data.",
    "Artificial intelligence enables machines to perform intelligent tasks.",
    "Deep learning is a branch of machine learning.",
    "Football is a popular sport played around the world.",
    "Natural language processing helps computers understand human language."
]

# Create TF-IDF embeddings
vectorizer = TfidfVectorizer()
document_embeddings = vectorizer.fit_transform(documents)

# Convert embeddings to float32
document_embeddings = document_embeddings.toarray().astype("float32")

# Create FAISS vector database
dimension = document_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)

# Store embeddings in FAISS
index.add(document_embeddings)

print("FAISS vector database created successfully.")
print("Number of documents:", index.ntotal)

# Get query
query = input("\nEnter your search query: ")

# Convert query to vector
query_embedding = vectorizer.transform([query])
query_embedding = query_embedding.toarray().astype("float32")

# Search top 3 documents
k = 3
distances, indices = index.search(query_embedding, k)

# Display results
print("\nSIMILARITY SEARCH RESULTS")
print("=========================")

for i in range(k):
    doc_index = indices[0][i]

    print("\nRank:", i + 1)
    print("Document:", documents[doc_index])
    print("Distance:", round(float(distances[0][i]), 4))
