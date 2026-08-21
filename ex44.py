import warnings
import os
import re

warnings.filterwarnings("ignore")
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import pipeline


# ============================================================
# 1. ENGINEERING KNOWLEDGE BASE
# ============================================================

questions = [
    "What is artificial intelligence?",
    "What is machine learning?",
    "What is deep learning?",
    "What is a neural network?",
    "What is Python?",
    "What is a database?",
    "What is DBMS?",
    "What is an operating system?",
    "What is computer networking?",
    "What is an IP address?",
    "What is a compiler?",
    "What is an algorithm?",
    "What is data structure?",
    "What is cloud computing?",
    "What is cybersecurity?",
    "What is debugging?",
    "How can I fix a Python syntax error?",
    "How can I fix a program that is running slowly?",
    "How can I improve program performance?",
    "What should I do if my program gives an error?"
]

answers = [
    "Artificial Intelligence (AI) is a field of computer science that enables machines to perform tasks that normally require human intelligence, such as learning, reasoning and decision making.",

    "Machine Learning (ML) is a branch of AI in which computers learn patterns from data and use those patterns to make predictions or decisions.",

    "Deep Learning is a type of machine learning that uses multi-layer neural networks to learn complex patterns from large amounts of data.",

    "A neural network is a machine learning model inspired by the human brain. It consists of interconnected nodes called neurons that process information.",

    "Python is a high-level, interpreted programming language widely used for AI, machine learning, data science, web development and automation.",

    "A database is an organized collection of data that can be stored, accessed, updated and managed efficiently.",

    "DBMS stands for Database Management System. It is software used to create, store, retrieve, update and manage data in databases.",

    "An operating system is system software that manages computer hardware and provides services for application programs. Examples include Windows, Linux and macOS.",

    "Computer networking is the process of connecting computers and devices so that they can communicate and share data and resources.",

    "An IP address is a unique address assigned to a device on a network so that the device can be identified and communicate with other devices.",

    "A compiler translates source code written in a programming language into machine code or another lower-level representation that a computer can execute.",

    "An algorithm is a step-by-step procedure used to solve a particular problem or perform a specific task.",

    "A data structure is a method of organizing and storing data so that it can be accessed and modified efficiently. Examples include arrays, stacks, queues and trees.",

    "Cloud computing provides computing resources such as servers, storage, databases and software over the internet.",

    "Cybersecurity is the practice of protecting computers, networks, applications and data from unauthorized access, attacks and damage.",

    "Debugging is the process of identifying, analyzing and fixing errors or bugs in a computer program.",

    "To fix a Python syntax error, carefully check the line mentioned in the error message. Look for missing brackets, colons, quotation marks, incorrect indentation or spelling mistakes.",

    "If a program is running slowly, check for unnecessary loops, repeated calculations, inefficient algorithms and excessive memory usage. Using a better algorithm can significantly improve performance.",

    "Program performance can be improved by selecting efficient algorithms and data structures, reducing unnecessary calculations, optimizing loops and avoiding unnecessary input/output operations.",

    "If a program gives an error, first read the error message and identify the line where the error occurred. Then check the variables, input values, syntax and logic around that line."
]


# ============================================================
# 2. NLP PREPROCESSING
# ============================================================

def preprocess(text):

    text = text.lower()

    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    text = re.sub(r'\s+', ' ', text)

    return text.strip()


processed_questions = []

for q in questions:
    processed_questions.append(preprocess(q))


# ============================================================
# 3. TF-IDF VECTOR CREATION
# ============================================================

vectorizer = TfidfVectorizer(
    stop_words="english"
)

question_vectors = vectorizer.fit_transform(processed_questions)


# ============================================================
# 4. LOAD PRE-TRAINED LANGUAGE MODEL
# ============================================================

print("Loading pre-trained language model...")

try:

    generator = pipeline(
        "text-generation",
        model="distilgpt2"
    )

    model_loaded = True

except Exception:

    model_loaded = False


# ============================================================
# 5. FIND MOST RELEVANT ANSWER
# ============================================================

def find_best_answer(user_question):

    processed_user_question = preprocess(user_question)

    user_vector = vectorizer.transform(
        [processed_user_question]
    )

    similarity = cosine_similarity(
        user_vector,
        question_vectors
    )

    best_index = similarity.argmax()

    best_score = similarity[0][best_index]

    # Minimum similarity required
    if best_score < 0.20:

        return None

    return answers[best_index]


# ============================================================
# 6. CHATBOT
# ============================================================

print()
print("=" * 60)
print("       ENGINEERING SUPPORT AI CHATBOT")
print("=" * 60)
print("Ask technical questions related to engineering.")
print("Type 'exit' to stop.")
print()


while True:

    user_question = input("Student: ").strip()

    if user_question.lower() == "exit":

        print("Chatbot: Thank you. Goodbye!")

        break


    if user_question == "":

        print("Chatbot: Please enter a technical question.")

        continue


    answer = find_best_answer(user_question)


    if answer is not None:

        print()
        print("Chatbot:", answer)
        print()

    else:

        print()
        print(
            "Chatbot: I could not find a relevant solution "
            "in my engineering knowledge base."
        )

        print(
            "Try asking about AI, machine learning, Python, "
            "DBMS, operating systems, networking, algorithms, "
            "data structures, cloud computing or cybersecurity."
        )

        print()
