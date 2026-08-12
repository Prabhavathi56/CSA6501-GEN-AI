# DOMAIN-SPECIFIC CHATBOT
# LangChain + FAISS Vector Database

from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from sklearn.feature_extraction.text import TfidfVectorizer


# -----------------------------------------
# 1. DOMAIN DOCUMENTS
# -----------------------------------------

documents = [
    Document(
        page_content="Artificial Intelligence is a branch of computer science that enables machines to perform tasks that normally require human intelligence."
    ),

    Document(
        page_content="Machine Learning is a subset of Artificial Intelligence that allows computers to learn patterns from data."
    ),

    Document(
        page_content="Deep Learning is a subset of Machine Learning that uses artificial neural networks with multiple layers."
    ),

    Document(
        page_content="Natural Language Processing enables computers to understand and process human language."
    ),

    Document(
        page_content="Generative AI can create new content such as text, images, audio, video and code."
    )
]

print("Domain documents loaded successfully.")


# -----------------------------------------
# 2. CREATE TF-IDF VECTORS
# -----------------------------------------

texts = [doc.page_content for doc in documents]

vectorizer = TfidfVectorizer()

vectorizer.fit(texts)


# -----------------------------------------
# 3. CUSTOM EMBEDDING CLASS
# -----------------------------------------

class TfidfEmbeddings:

    def embed_documents(self, texts):
        return vectorizer.transform(texts).toarray().tolist()

    def embed_query(self, text):
        return vectorizer.transform([text]).toarray()[0].tolist()


embeddings = TfidfEmbeddings()


# -----------------------------------------
# 4. CREATE FAISS VECTOR DATABASE
# -----------------------------------------

vector_db = FAISS.from_documents(
    documents,
    embeddings
)

print("FAISS vector database created successfully.")


# -----------------------------------------
# 5. CHATBOT
# -----------------------------------------

print("\n======================================")
print("      AI DOMAIN-SPECIFIC CHATBOT")
print("======================================")
print("Domain: Artificial Intelligence")
print("Type 'exit' to stop the chatbot.")


while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    # Retrieve top 2 relevant documents
    results = vector_db.similarity_search(
        question,
        k=2
    )

    print("\nChatbot:")

    if len(results) == 0:

        print("Sorry, I could not find relevant information.")

    else:

        for result in results:
            print("-", result.page_content)
