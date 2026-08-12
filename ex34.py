from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Documents
documents = [
    "Python is a programming language used for software development.",
    "Machine learning allows computers to learn from data.",
    "Artificial intelligence helps machines perform intelligent tasks.",
    "Deep learning is a part of machine learning.",
    "Football is a popular sport played by many people."
]

# Create embeddings for documents
vectorizer = TfidfVectorizer()
document_embeddings = vectorizer.fit_transform(documents)

# Get query
query = input("Enter your search query: ")

# Create embedding for query
query_embedding = vectorizer.transform([query])

# Calculate cosine similarity
similarity = cosine_similarity(
    query_embedding,
    document_embeddings
)[0]

# Rank documents
ranked_results = sorted(
    zip(documents, similarity),
    key=lambda x: x[1],
    reverse=True
)

# Display results
print("\nSEMANTIC SEARCH RESULTS")
print("=======================")

for rank, (document, score) in enumerate(ranked_results, 1):
    print(f"\nRank {rank}")
    print("Document:", document)
    print("Cosine Similarity:", round(score, 4))
