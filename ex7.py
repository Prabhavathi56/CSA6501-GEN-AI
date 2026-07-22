from transformers import pipeline

# Load pre-trained sentiment analysis model
classifier = pipeline("sentiment-analysis")

# Test sentence
text = "I love learning Artificial Intelligence."

# Perform sentiment analysis
result = classifier(text)

print("Text:", text)
print("Sentiment:", result)
