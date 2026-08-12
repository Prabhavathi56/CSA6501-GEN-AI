from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Documents
documents = [
    "Python is a popular programming language.",
    "Machine learning allows computers to learn from data.",
    "Artificial intelligence enables machines to perform intelligent tasks.",
    "Football is a popular sport played around the world.",
    "Deep learning is a branch of machine learning."
]

# Create text embeddings using TF-IDF
vectorizer = TfidfVectorizer()
document_embeddings = vectorizer.fit_transform(documents)

# Get query from user
query = input("Enter your search query: ")

# Convert query into embedding
query_embedding = vectorizer.transform([query])

# Calculate similarity
similarity_scores = cosine_similarity(
    query_embedding,
    document_embeddings
)[0]

# Rank documents
results = sorted(
    zip(documents, similarity_scores),
    key=lambda x: x[1],
    reverse=True
)

# Display results
print("\nSEMANTIC SIMILARITY SEARCH")
print("==========================")

for i, (document, score) in enumerate(results, 1):
    print(f"\n{i}. Similarity Score: {score:.4f}")
    print("   Document:", document)
