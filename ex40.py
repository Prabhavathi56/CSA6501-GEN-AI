# CONTEXT-AWARE CHATBOT USING LANGCHAIN, RETRIEVAL AND LLM

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from google import genai


# ==========================================
# 1. GEMINI API KEY
# ==========================================

API_KEY = ""

client = genai.Client(api_key=API_KEY)


# ==========================================
# 2. DOMAIN DOCUMENTS
# ==========================================

documents = [
    "Artificial Intelligence is a branch of computer science that enables machines to perform tasks that normally require human intelligence.",

    "Machine Learning is a subset of Artificial Intelligence that allows computers to learn patterns from data.",

    "Deep Learning is a subset of Machine Learning that uses artificial neural networks with multiple layers.",

    "Natural Language Processing enables computers to understand and process human language.",

    "Generative AI can generate new content such as text, images, audio, video and code."
]

print("Documents loaded successfully.")


# ==========================================
# 3. CREATE DOCUMENT EMBEDDINGS
# ==========================================

vectorizer = TfidfVectorizer()

document_vectors = vectorizer.fit_transform(documents)

print("Document embeddings created successfully.")


# ==========================================
# 4. CONVERSATION MEMORY
# ==========================================

chat_history = []


# ==========================================
# 5. START CHATBOT
# ==========================================

print("\n======================================")
print("       CONTEXT-AWARE AI CHATBOT")
print("======================================")
print("Domain: Artificial Intelligence")
print("Type 'exit' to stop.")


while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        print("Chatbot: Goodbye!")
        break


    # ======================================
    # 6. QUERY EMBEDDING
    # ======================================

    query_vector = vectorizer.transform([question])


    # ======================================
    # 7. RETRIEVAL
    # ======================================

    similarity_scores = cosine_similarity(
        query_vector,
        document_vectors
    )[0]


    # Get top 2 relevant documents
    top_indices = similarity_scores.argsort()[-2:][::-1]


    context = ""

    for index in top_indices:
        context += documents[index] + "\n"


    # ======================================
    # 8. CONVERSATION HISTORY
    # ======================================

    history = ""

    for user_question, bot_answer in chat_history:

        history += f"""
User: {user_question}
Assistant: {bot_answer}
"""


    # ======================================
    # 9. CREATE LLM PROMPT
    # ======================================

    prompt = f"""
You are a context-aware chatbot specializing in
Artificial Intelligence.

Use the retrieved information and previous conversation
to answer the user's question.

RETRIEVED INFORMATION:
{context}

PREVIOUS CONVERSATION:
{history}

CURRENT QUESTION:
{question}

Rules:
1. Give a simple and clear answer.
2. Use the retrieved information.
3. Use previous conversation when the user asks a follow-up question.
4. Do not invent information.
"""


    # ======================================
    # 10. GENERATE ANSWER
    # ======================================

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        answer = response.text

        print("\nChatbot:", answer)


        # ==================================
        # 11. STORE CONVERSATION
        # ==================================

        chat_history.append(
            (question, answer)
        )


    except Exception as e:

        print("\nGemini API Error:")
        print(e)
