import tkinter as tk
from tkinter import scrolledtext

def summarize_text():
    text = input_box.get("1.0", tk.END).strip()

    if text == "":
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, "Please enter some text to summarize.")
        return

    # Split text into sentences
    sentences = text.replace("!", ".").replace("?", ".").split(".")

    sentences = [s.strip() for s in sentences if s.strip()]

    # Simple summarization
    if len(sentences) <= 2:
        summary = text
    else:
        # Select important-looking sentences
        summary = sentences[0] + ". "

        if len(sentences) >= 3:
            summary += sentences[len(sentences) // 2] + ". "

        summary += sentences[-1] + "."

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, summary)


def clear_text():
    input_box.delete("1.0", tk.END)
    output_box.delete("1.0", tk.END)


# Main window
window = tk.Tk()
window.title("AI Text Summarization Application")
window.geometry("800x650")

# Title
title = tk.Label(
    window,
    text="AI Text Summarization Application",
    font=("Arial", 22, "bold")
)
title.pack(pady=15)

# Input label
input_label = tk.Label(
    window,
    text="Enter Text:",
    font=("Arial", 13, "bold")
)
input_label.pack()

# Input box
input_box = scrolledtext.ScrolledText(
    window,
    width=85,
    height=12,
    font=("Arial", 11)
)
input_box.pack(pady=10)

# Buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

summarize_button = tk.Button(
    button_frame,
    text="Summarize Text",
    command=summarize_text,
    font=("Arial", 12, "bold")
)
summarize_button.pack(side=tk.LEFT, padx=10)

clear_button = tk.Button(
    button_frame,
    text="Clear",
    command=clear_text,
    font=("Arial", 12, "bold")
)
clear_button.pack(side=tk.LEFT, padx=10)

# Output label
output_label = tk.Label(
    window,
    text="Summary:",
    font=("Arial", 13, "bold")
)
output_label.pack()

# Output box
output_box = scrolledtext.ScrolledText(
    window,
    width=85,
    height=10,
    font=("Arial", 11)
)
output_box.pack(pady=10)

# Start application
window.mainloop()
