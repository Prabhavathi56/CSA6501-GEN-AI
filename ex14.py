from transformers import pipeline

# Load Question Answering pipeline with a pre-trained model
qa = pipeline(
    task="question-answering",
    model="distilbert-base-cased-distilled-squad",
    tokenizer="distilbert-base-cased-distilled-squad"
)

# Context and Question
context = """
Artificial Intelligence is a branch of computer science that enables machines
to perform tasks requiring human intelligence.
"""

question = "What is Artificial Intelligence?"

# Get the answer
result = qa(question=question, context=context)

# Print the result
print("Question:", question)
print("Answer:", result["answer"])
print("Score:", result["score"])
