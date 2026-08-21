import warnings
import os

warnings.filterwarnings("ignore")
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

from transformers import pipeline

# -------------------------------------------------
# LOAD PRE-TRAINED LANGUAGE MODEL
# -------------------------------------------------
chatbot = pipeline(
    "text-generation",
    model="distilgpt2"
)

# -------------------------------------------------
# COLLEGE INFORMATION
# -------------------------------------------------
college_info = {
    "courses": "The college offers B.Tech programs in Computer Science and Engineering, Artificial Intelligence, Artificial Intelligence and Data Science, Electronics and Communication Engineering, Mechanical Engineering, and Civil Engineering.",

    "hostel": "Yes, the college provides hostel facilities for students.",

    "library": "The college provides library facilities for students with academic books and study resources.",

    "laboratory": "The college provides laboratory facilities for practical learning and academic activities.",

    "placement": "Yes, the college has a placement cell that provides training, career guidance, and placement assistance.",

    "exam": "The examination cell conducts internal examinations and semester examinations.",

    "transport": "The college provides transportation facilities for students.",

    "sports": "The college provides sports facilities for students.",

    "attendance": "Students must maintain the attendance percentage required by the college regulations.",

    "departments": "The college has departments including Computer Science and Engineering, Artificial Intelligence, Artificial Intelligence and Data Science, Electronics and Communication Engineering, Mechanical Engineering, and Civil Engineering."
}

# -------------------------------------------------
# KEYWORDS FOR QUESTIONS
# -------------------------------------------------
keywords = {
    "courses": [
        "course", "courses", "program", "programs",
        "branch", "branches", "degree", "degrees"
    ],

    "hostel": [
        "hostel", "accommodation", "stay", "room"
    ],

    "library": [
        "library", "books", "study"
    ],

    "laboratory": [
        "lab", "labs", "laboratory", "laboratories"
    ],

    "placement": [
        "placement", "placements", "job", "jobs",
        "career", "company", "companies"
    ],

    "exam": [
        "exam", "exams", "examination",
        "semester", "internal"
    ],

    "transport": [
        "transport", "bus", "buses"
    ],

    "sports": [
        "sport", "sports", "game", "games"
    ],

    "attendance": [
        "attendance", "absent", "absence"
    ],

    "departments": [
        "department", "departments"
    ]
}

# -------------------------------------------------
# FUNCTION TO FIND ANSWER
# -------------------------------------------------
def find_answer(question):

    question = question.lower()

    for category, words in keywords.items():

        for word in words:

            if word in question:
                return college_info[category]

    return None


# -------------------------------------------------
# CHATBOT
# -------------------------------------------------
print("=" * 50)
print("        AI ENGINEERING COLLEGE CHATBOT")
print("=" * 50)
print("Ask questions about the engineering college.")
print("Type 'exit' to stop.\n")

while True:

    question = input("Student: ").strip()

    if question.lower() == "exit":
        print("Chatbot: Thank you. Goodbye!")
        break

    if question == "":
        print("Chatbot: Please enter a question.")
        continue

    answer = find_answer(question)

    if answer is not None:

        print("Chatbot:", answer)

    else:

        print(
            "Chatbot: Sorry, I don't have information "
            "about that. Please ask about courses, hostel, "
            "library, laboratories, placements, exams, "
            "transport, sports or attendance."
        )
