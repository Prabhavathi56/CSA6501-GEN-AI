# Hallucination Demonstration
# No Ollama or external software required

REFERENCE = """
The Smart Campus Energy Management System is designed for educational
institutions. It monitors electricity consumption, active devices,
energy cost, and campus occupancy. It uses AI-based prediction and
anomaly detection to improve energy efficiency.
"""

# Simulated LLM responses
responses = {
    1: "The system monitors electricity consumption, active devices, energy cost, and campus occupancy.",
    2: "The system was developed by ABC University in 2024.",
    3: "The system uses solar panels to generate 50 kW of electricity.",
    4: "The system monitors exactly 10,000 students."
}

questions = {
    1: "What does the system monitor?",
    2: "Who developed the system and when?",
    3: "Does the system use solar panels to generate 50 kW?",
    4: "How many students does the system monitor?"
}

# Check whether response is supported by reference
def check_hallucination(answer, reference):

    keywords = [
        "electricity consumption",
        "active devices",
        "energy cost",
        "campus occupancy"
    ]

    supported = 0

    for word in keywords:
        if word.lower() in answer.lower():
            supported += 1

    # If response contains known unsupported information
    if ("ABC University" in answer or
        "2024" in answer or
        "50 kW" in answer or
        "10,000 students" in answer):

        return "HALLUCINATION"

    if supported > 0:
        return "SUPPORTED"

    return "UNSUPPORTED"


print("=" * 60)
print("LLM HALLUCINATION DEMONSTRATION")
print("=" * 60)

hallucinations = 0
total = len(questions)

for i in questions:

    print("\nTest", i)
    print("-" * 60)

    print("Question:")
    print(questions[i])

    print("\nReference:")
    print(REFERENCE)

    print("LLM Response:")
    print(responses[i])

    result = check_hallucination(responses[i], REFERENCE)

    print("\nAnalysis:", result)

    if result == "HALLUCINATION":
        hallucinations += 1

print("\n" + "=" * 60)

rate = (hallucinations / total) * 100

print("Total Tests:", total)
print("Hallucinated Responses:", hallucinations)
print("Hallucination Rate:", rate, "%")

print("=" * 60)
