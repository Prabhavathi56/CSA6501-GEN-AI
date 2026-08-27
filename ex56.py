import tkinter as tk
from tkinter import scrolledtext


def translate_text():
    text = input_box.get("1.0", tk.END).strip()
    language = language_var.get()

    if text == "":
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, "Please enter some text.")
        return

    # Simple translation examples
    translations = {
        "Tamil": {
            "hello": "வணக்கம்",
            "how are you": "நீங்கள் எப்படி இருக்கிறீர்கள்?",
            "good morning": "காலை வணக்கம்",
            "thank you": "நன்றி",
            "artificial intelligence": "செயற்கை நுண்ணறிவு"
        },

        "Telugu": {
            "hello": "నమస్కారం",
            "how are you": "మీరు ఎలా ఉన్నారు?",
            "good morning": "శుభోదయం",
            "thank you": "ధన్యవాదాలు",
            "artificial intelligence": "కృత్రిమ మేధస్సు"
        },

        "Hindi": {
            "hello": "नमस्ते",
            "how are you": "आप कैसे हैं?",
            "good morning": "सुप्रभात",
            "thank you": "धन्यवाद",
            "artificial intelligence": "कृत्रिम बुद्धिमत्ता"
        }
    }

    key = text.lower()

    if key in translations[language]:
        result = translations[language][key]
    else:
        result = "Translation not available for this sentence."

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, result)


def paraphrase_text():
    text = input_box.get("1.0", tk.END).strip()

    if text == "":
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, "Please enter some text.")
        return

    # Simple paraphrasing
    sentences = {
        "Artificial intelligence is very useful.":
            "Artificial intelligence is extremely helpful.",

        "Python is easy to learn.":
            "Python is a simple programming language to learn.",

        "Machine learning is a part of AI.":
            "Machine learning is an important branch of artificial intelligence.",

        "The computer processes data.":
            "The computer analyzes and processes information."
    }

    if text in sentences:
        result = sentences[text]
    else:
        result = "Paraphrased text: " + text

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, result)


def clear_text():
    input_box.delete("1.0", tk.END)
    output_box.delete("1.0", tk.END)


# Main window
window = tk.Tk()
window.title("Text Translation and Paraphrasing")
window.geometry("850x650")


# Title
title = tk.Label(
    window,
    text="Text Translation and Paraphrasing",
    font=("Arial", 22, "bold")
)
title.pack(pady=20)


# Input
input_label = tk.Label(
    window,
    text="Enter Text:",
    font=("Arial", 13, "bold")
)
input_label.pack()

input_box = scrolledtext.ScrolledText(
    window,
    width=90,
    height=8,
    font=("Arial", 11)
)
input_box.pack(pady=10)


# Language selection
language_var = tk.StringVar()
language_var.set("Tamil")

language_label = tk.Label(
    window,
    text="Select Translation Language:",
    font=("Arial", 12, "bold")
)
language_label.pack()

language_menu = tk.OptionMenu(
    window,
    language_var,
    "Tamil",
    "Telugu",
    "Hindi"
)
language_menu.pack(pady=5)


# Buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=15)

translate_button = tk.Button(
    button_frame,
    text="Translate",
    command=translate_text,
    font=("Arial", 12, "bold")
)
translate_button.pack(side=tk.LEFT, padx=10)

paraphrase_button = tk.Button(
    button_frame,
    text="Paraphrase",
    command=paraphrase_text,
    font=("Arial", 12, "bold")
)
paraphrase_button.pack(side=tk.LEFT, padx=10)

clear_button = tk.Button(
    button_frame,
    text="Clear",
    command=clear_text,
    font=("Arial", 12, "bold")
)
clear_button.pack(side=tk.LEFT, padx=10)


# Output
output_label = tk.Label(
    window,
    text="Output:",
    font=("Arial", 13, "bold")
)
output_label.pack()

output_box = scrolledtext.ScrolledText(
    window,
    width=90,
    height=10,
    font=("Arial", 11)
)
output_box.pack(pady=10)


window.mainloop()
