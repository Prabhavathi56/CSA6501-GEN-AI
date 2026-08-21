import warnings
import os

warnings.filterwarnings("ignore")
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


# ==========================================================
# AI ENGINEERING DOCUMENT SUMMARIZER
# ==========================================================

print("=" * 60)
print("       AI ENGINEERING DOCUMENT SUMMARIZER")
print("=" * 60)

print("\nLoading pre-trained language model...")
print("Please wait...")


# ==========================================================
# LOAD PRE-TRAINED FLAN-T5 MODEL
# ==========================================================

model_name = "google/flan-t5-small"

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

print("Model loaded successfully!")


# ==========================================================
# ENGINEERING DOCUMENT
# ==========================================================

document = """
Artificial Intelligence is transforming modern engineering by
providing intelligent methods for solving complex problems.
Machine learning algorithms can analyze large datasets and
identify useful patterns for prediction and decision-making.
Deep learning uses neural networks with multiple layers to
process complex information such as images, speech, and sensor
data.

In mechanical engineering, AI can be used for predictive
maintenance, fault detection, and manufacturing automation.
In civil engineering, AI helps monitor structures, analyze
construction data, and improve project planning.

In electrical and electronics engineering, AI is used for
smart grids, automated control systems, signal processing,
and fault diagnosis.

AI also plays an important role in robotics and autonomous
systems. Robots can use computer vision and machine learning
to recognize objects, navigate environments, and perform
industrial tasks.

Engineers can combine AI with Internet of Things devices
to collect real-time sensor data and make intelligent
decisions.

However, implementing AI in engineering requires high-quality
data, suitable algorithms, sufficient computing resources,
and careful testing. Engineers must also consider security,
reliability, privacy, and ethical issues.
"""


# ==========================================================
# DISPLAY DOCUMENT
# ==========================================================

print("\n" + "=" * 60)
print("ENGINEERING DOCUMENT")
print("=" * 60)

print(document)


# ==========================================================
# CREATE SUMMARIZATION PROMPT
# ==========================================================

prompt = """
Summarize the following engineering document in a short,
clear and meaningful paragraph.

Document:
""" + document


# ==========================================================
# TOKENIZE INPUT
# ==========================================================

inputs = tokenizer(
    prompt,
    return_tensors="pt",
    max_length=512,
    truncation=True
)


# ==========================================================
# GENERATE SUMMARY
# ==========================================================

print("\n" + "=" * 60)
print("GENERATING SUMMARY...")
print("=" * 60)

outputs = model.generate(
    **inputs,
    max_new_tokens=100,
    min_new_tokens=30,
    num_beams=4,
    early_stopping=True
)


# ==========================================================
# DECODE SUMMARY
# ==========================================================

summary = tokenizer.decode(
    outputs[0],
    skip_special_tokens=True
)


# ==========================================================
# DISPLAY SUMMARY
# ==========================================================

print("\n" + "=" * 60)
print("GENERATED SUMMARY")
print("=" * 60)

print(summary)

print("\n" + "=" * 60)
print("SUMMARY COMPLETED SUCCESSFULLY")
print("=" * 60)
