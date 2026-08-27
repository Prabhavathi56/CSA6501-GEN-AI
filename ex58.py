import tkinter as tk
from tkinter import scrolledtext
import requests


def ask_question():
    question = question_box.get("1.0", tk.END).strip()

    if question == "":
        answer_box.delete("1.0", tk.END)
        answer_box.insert(tk.END, "Please enter a question.")
        return

    answer_box.delete("1.0", tk.END)
    answer_box.insert(tk.END, "Getting answer...")

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2",
                "prompt": question,
                "stream": False
            }
        )

        if response.status_code == 200:
            data = response.json()

            answer_box.delete("1.0", tk.END)
            answer_box.insert(tk.END, data["response"])

        else:
            answer_box.delete("1.0", tk.END)
            answer_box.insert(tk.END, "Error connecting to Ollama.")

    except:
        answer_box.delete("1.0", tk.END)
        answer_box.insert(
            tk.END,
            "Ollama is not running.\n"
            "Please start Ollama and try again."
        )


def clear_text():
    question_box.delete("1.0", tk.END)
    answer_box.delete("1.0", tk.END)


# Window
window = tk.Tk()
window.title("Question Answering using Local LLM")
window.geometry("800x600")

# Title
title = tk.Label(
    window,
    text="Question Answering using Local LLM",
    font=("Arial", 20, "bold")
)
title.pack(pady=20)

# Question
question_label = tk.Label(
    window,
    text="Enter your Question:",
    font=("Arial", 13, "bold")
)
question_label.pack()

question_box = scrolledtext.ScrolledText(
    window,
    width=85,
    height=8,
    font=("Arial", 11)
)
question_box.pack(pady=10)

# Buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

ask_button = tk.Button(
    button_frame,
    text="Ask Question",
    command=ask_question,
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

# Answer
answer_label = tk.Label(
    window,
    text="Answer:",
    font=("Arial", 13, "bold")
)
answer_label.pack()

answer_box = scrolledtext.ScrolledText(
    window,
    width=85,
    height=15,
    font=("Arial", 11)
)
answer_box.pack(pady=10)

window.mainloop()
