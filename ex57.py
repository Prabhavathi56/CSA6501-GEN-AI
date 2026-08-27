import tkinter as tk
from tkinter import scrolledtext


def generate_text():
    prompt = input_box.get("1.0", tk.END).strip()

    if prompt == "":
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, "Please enter a prompt.")
        return

    p = prompt.lower()

    if "artificial intelligence" in p:
        answer = """Artificial Intelligence (AI) is a branch of
computer science that enables machines to perform tasks
that normally require human intelligence. AI is used in
healthcare, education, transportation and many other fields."""

    elif "machine learning" in p:
        answer = """Machine Learning is a branch of Artificial
Intelligence that allows computers to learn patterns from
data and make predictions or decisions."""

    elif "python" in p:
        answer = """Python is a high-level programming language
used for artificial intelligence, machine learning, data
science, web development and automation."""

    elif "technology" in p:
        answer = """Technology refers to the use of scientific
knowledge, tools and techniques to solve problems and make
human activities easier and more efficient."""

    else:
        answer = """Generated Text:

Your prompt is:
""" + prompt + """

This application generated a response based on the
information available in its knowledge base."""

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, answer)


def clear_text():
    input_box.delete("1.0", tk.END)
    output_box.delete("1.0", tk.END)


# Main window
window = tk.Tk()
window.title("Text Generation Application")
window.geometry("800x600")

# Title
title = tk.Label(
    window,
    text="Local Text Generation Application",
    font=("Arial", 22, "bold")
)
title.pack(pady=20)

# Prompt
prompt_label = tk.Label(
    window,
    text="Enter your Prompt:",
    font=("Arial", 13, "bold")
)
prompt_label.pack()

input_box = scrolledtext.ScrolledText(
    window,
    width=85,
    height=8,
    font=("Arial", 11)
)
input_box.pack(pady=10)

# Buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

generate_button = tk.Button(
    button_frame,
    text="Generate Text",
    command=generate_text,
    font=("Arial", 12, "bold")
)
generate_button.pack(side=tk.LEFT, padx=10)

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
    text="Generated Text:",
    font=("Arial", 13, "bold")
)
output_label.pack()

output_box = scrolledtext.ScrolledText(
    window,
    width=85,
    height=15,
    font=("Arial", 11)
)
output_box.pack(pady=10)

window.mainloop()
