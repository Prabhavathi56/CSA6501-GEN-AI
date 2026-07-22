from transformers import pipeline

# Load the pre-trained sentiment analysis pipeline
classifier = pipeline("sentiment-analysis")

# Input text
text = "I really enjoyed learning about Transformers!"

# Perform sentiment analysis
result = classifier(text)

# Display the result
print("Input Text:", text)
print("Sentiment:", result[0]["label"])
print("Confidence Score:", result[0]["score"])
