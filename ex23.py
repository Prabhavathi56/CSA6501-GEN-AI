# Experiment: Zero-shot, One-shot, and Few-shot Prompting
# Task: Summarize an article into 50 words

# Sample Article
article = """
Artificial Intelligence (AI) is transforming various industries by improving
automation, decision-making, and efficiency. In healthcare, AI helps doctors
diagnose diseases, discover medicines, and provide personalized treatments.
In education, AI enables smart learning platforms and personalized teaching.
Businesses use AI for customer service, data analysis, and prediction.
AI continues to grow and create new opportunities while also raising concerns
about privacy, ethics, and responsible usage.
"""

# ---------------- Zero-shot Prompt ----------------

zero_shot_prompt = f"""
Summarize the following article into exactly 50 words:

Article:
{article}
"""

zero_shot_output = """
Artificial Intelligence is changing industries through automation and better
decision-making. It supports healthcare by diagnosing diseases and developing
medicines, improves education with personalized learning, and helps businesses
through data analysis. Although AI creates opportunities, concerns about
privacy, ethics, and responsible use must be addressed.
"""


# ---------------- One-shot Prompt ----------------

one_shot_prompt = f"""
Example:

Article:
Machine learning helps computers learn from data and improve performance.
It is used in recommendation systems, healthcare, and financial analysis.

Summary:
Machine learning enables computers to learn from data and is applied in
healthcare, recommendations, and finance.

Now summarize this article into 50 words:

Article:
{article}
"""

one_shot_output = """
AI is revolutionizing industries by improving automation and decision-making.
It assists healthcare through diagnosis and drug discovery, supports education
with personalized learning, and enhances businesses using data analysis.
However, AI development also requires attention to privacy, ethics, and
responsible implementation.
"""


# ---------------- Few-shot Prompt ----------------

few_shot_prompt = f"""
Example 1:

Article:
Cloud computing provides online storage and computing resources.
It improves scalability, flexibility, and reduces infrastructure costs.

Summary:
Cloud computing offers flexible and scalable computing resources while
reducing costs for organizations.

Example 2:

Article:
Renewable energy sources reduce pollution and provide sustainable power.
Solar and wind energy are clean alternatives to fossil fuels.

Summary:
Renewable energy provides clean and sustainable power while reducing
environmental pollution.

Now summarize this article into 50 words:

Article:
{article}
"""

few_shot_output = """
Artificial Intelligence is transforming healthcare, education, and businesses
by improving automation, analysis, and decision-making. AI helps diagnose
diseases, personalize learning, and predict business trends. Despite its
benefits, challenges related to privacy, ethics, and responsible usage need
proper management.
"""


# ---------------- Comparison ----------------

print("="*60)
print("ZERO-SHOT SUMMARY")
print("="*60)
print(zero_shot_output)

print("\n"+"="*60)
print("ONE-SHOT SUMMARY")
print("="*60)
print(one_shot_output)

print("\n"+"="*60)
print("FEW-SHOT SUMMARY")
print("="*60)
print(few_shot_output)


print("\n\nCOMPARISON")
print("="*60)

print("""
Technique      Accuracy       Completeness       Readability

Zero-shot      Good           Moderate           Good
One-shot       Better         Good               Very Good
Few-shot       Highest        Highest            Very Good

Conclusion:
Few-shot prompting produces the best summary because examples guide the model
to understand the required format, important points, and writing style.
""")
