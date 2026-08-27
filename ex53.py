import tkinter as tk
from tkinter import scrolledtext

def generate_text():
    prompt = input_box.get("1.0", tk.END).strip()

    if prompt == "":
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, "Please enter a prompt.")
        return

    prompt_lower = prompt.lower()

    if "artificial intelligence" in prompt_lower:
        answer = """Artificial Intelligence (AI) is a technology
that enables computers to perform tasks that normally require
human intelligence. AI is used in areas such as learning,
reasoning, image recognition and language processing."""

    elif "machine learning" in prompt_lower:
        answer = """Machine Learning is a branch of Artificial
Intelligence. It allows computers to learn patterns from data
and make predictions without being explicitly programmed."""

    elif "python" in prompt_lower:
        answer = """Python is a high-level programming language.
It is widely used for artificial intelligence, machine learning,
data science, web development and automation."""

    elif "computer" in prompt_lower:
        answer = """A computer is an electronic device that
processes data according to instructions. It can perform
calculations, store information and communicate with other
devices."""

    else:
        answer = """Generated Response:

You entered:
""" + prompt + """

This application processed your prompt successfully."""

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, answer)


# Main window
window = tk.Tk()
window.title("AI Text Generation Application")
window.geometry("700x500")

title = tk.Label(
    window,
    text="AI Text Generation Application",
    font=("Arial", 20, "bold")
)
title.pack(pady=15)

label1 = tk.Label(
    window,
    text="Enter your prompt:",
    font=("Arial", 12)
)
label1.pack()

input_box = scrolledtext.ScrolledText(
    window,
    width=75,
    height=6,
    font=("Arial", 11)
)
input_box.pack(pady=10)

button = tk.Button(
    window,
    text="Generate Text",
    command=generate_text,
    font=("Arial", 12, "bold")
)
button.pack(pady=10)

label2 = tk.Label(
    window,
    text="Generated Text:",
    font=("Arial", 12)
)
label2.pack()

output_box = scrolledtext.ScrolledText(
    window,
    width=75,
    height=12,
    font=("Arial", 11)
)
output_box.pack(pady=10)

window.mainloop()
