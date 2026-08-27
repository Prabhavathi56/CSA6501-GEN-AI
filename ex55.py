
import tkinter as tk
from tkinter import scrolledtext


def answer_question():
    question = question_box.get("1.0", tk.END).strip().lower()

    if question == "":
        answer_box.delete("1.0", tk.END)
        answer_box.insert(tk.END, "Please enter a question.")
        return

    # Question answering
    if "what is artificial intelligence" in question or "what is ai" in question:
        answer = """Artificial Intelligence (AI) is a branch of
computer science that enables machines to perform tasks
that normally require human intelligence."""

    elif "what is machine learning" in question:
        answer = """Machine Learning is a branch of Artificial
Intelligence that enables computers to learn from data
and make predictions or decisions."""

    elif "what is python" in question:
        answer = """Python is a high-level programming language
that is widely used for artificial intelligence, machine
learning, web development and data science."""

    elif "what is computer" in question:
        answer = """A computer is an electronic device that
accepts data, processes it, stores it and produces useful
information as output."""

    elif "what is deep learning" in question:
        answer = """Deep Learning is a part of Machine Learning
that uses neural networks with multiple layers to learn
complex patterns from large amounts of data."""

    elif "what is database" in question:
        answer = """A database is an organized collection of
data that can be stored, managed and retrieved efficiently."""

    elif "what is internet" in question:
        answer = """The Internet is a worldwide network of
connected computers and devices that communicate and
share information."""

    elif "who are you" in question:
        answer = """I am a simple Python-based Question
Answering System developed using Tkinter."""

    elif "hello" in question or "hi" in question:
        answer = "Hello! How can I help you?"

    else:
        answer = """Sorry, I don't have an answer for that
question in my knowledge base.

Try asking questions about:
• Artificial Intelligence
• Machine Learning
• Python
• Deep Learning
• Computer
• Database
• Internet"""


    answer_box.delete("1.0", tk.END)
    answer_box.insert(tk.END, answer)


def clear_text():
    question_box.delete("1.0", tk.END)
    answer_box.delete("1.0", tk.END)


# Create window
window = tk.Tk()
window.title("Question Answering System")
window.geometry("800x600")


# Title
title = tk.Label(
    window,
    text="Question Answering System",
    font=("Arial", 22, "bold")
)
title.pack(pady=20)


# Question label
question_label = tk.Label(
    window,
    text="Enter your Question:",
    font=("Arial", 13, "bold")
)
question_label.pack()


# Question input
question_box = scrolledtext.ScrolledText(
    window,
    width=85,
    height=7,
    font=("Arial", 11)
)
question_box.pack(pady=10)


# Buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=10)


ask_button = tk.Button(
    button_frame,
    text="Ask Question",
    command=answer_question,
    font=("Arial", 12, "bold")
)
ask_button.pack(side=tk.LEFT, padx=10)


clear_button = tk.Button(
    button_frame,
    text="Clear",
    command=clear_text,
    font=("Arial", 12, "bold")
)
clear_button.pack(side=tk.LEFT, padx=10)


# Answer label
answer_label = tk.Label(
    window,
    text="Answer:",
    font=("Arial", 13, "bold")
)
answer_label.pack()


# Answer output
answer_box = scrolledtext.ScrolledText(
    window,
    width=85,
    height=12,
    font=("Arial", 11)
)
answer_box.pack(pady=10)


# Run application
window.mainloop()
