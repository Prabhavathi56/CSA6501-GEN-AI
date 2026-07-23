# Experiment: Zero-shot, One-shot, and Few-shot Prompting
# Task: Generate a promotional social media post for an AI Workshop


# ---------------- Zero-shot Prompt ----------------

zero_shot_prompt = """
Create a promotional social media post for an AI Workshop.
Include an attractive headline, key topics, benefits, and a call to action.
"""

zero_shot_output = """
🚀 Unlock the Future with Artificial Intelligence! 🤖

Join our AI Workshop and explore the exciting world of Artificial
Intelligence, Machine Learning, and Generative AI. Learn about real-world
AI applications, hands-on projects, and the latest technologies from experts.

✨ Gain practical knowledge
✨ Build AI skills
✨ Explore career opportunities

Don't miss this opportunity to upgrade your skills and become future-ready!

Register now and start your AI journey today! 🚀
"""


# ---------------- One-shot Prompt ----------------

one_shot_prompt = """
Example:

Topic: Python Programming Workshop

Post:
🐍 Learn Python Programming!

Join our beginner-friendly Python workshop to learn coding basics,
automation, and real-world applications. Get hands-on experience and
improve your programming skills.

Register today!

Now create a promotional social media post for:
AI Workshop
"""

one_shot_output = """
🤖 Discover the Power of Artificial Intelligence!

Join our AI Workshop and learn how AI is transforming industries.
Explore Machine Learning, Deep Learning, Generative AI, and practical
AI applications through interactive sessions.

📌 What You Will Learn:
✔ AI fundamentals
✔ Machine Learning concepts
✔ Real-world AI projects

Build your skills and prepare for the future of technology.

Enroll now and begin your AI learning journey! 🚀
"""


# ---------------- Few-shot Prompt ----------------

few_shot_prompt = """
Example 1:

Topic: Data Science Workshop

Post:
📊 Become a Data Science Expert!

Learn data analysis, visualization, and machine learning techniques.
Join our hands-on workshop and enhance your career opportunities.

Register now!


Example 2:

Topic: Cyber Security Workshop

Post:
🔐 Protect the Digital World!

Join our cybersecurity workshop to learn about ethical hacking,
network security, and online safety practices.

Start your security journey today!


Now create a promotional social media post for:
AI Workshop
"""

few_shot_output = """
🚀 AI Workshop 2026: Build the Future with Artificial Intelligence! 🤖

Are you ready to explore the world of AI?

Join our exclusive AI Workshop and gain hands-on experience in
Artificial Intelligence, Machine Learning, Deep Learning, and Generative AI.

🌟 Workshop Highlights:
✅ Learn AI concepts from experts
✅ Work on real-world AI applications
✅ Develop practical skills
✅ Discover career opportunities in AI

Whether you are a student or technology enthusiast, this workshop
will help you take your AI skills to the next level.

📅 Register today and start your journey into the world of AI! 🚀
"""


# ---------------- Display Results ----------------

print("="*60)
print("ZERO-SHOT PROMPT OUTPUT")
print("="*60)
print(zero_shot_output)


print("\n"+"="*60)
print("ONE-SHOT PROMPT OUTPUT")
print("="*60)
print(one_shot_output)


print("\n"+"="*60)
print("FEW-SHOT PROMPT OUTPUT")
print("="*60)
print(few_shot_output)


# ---------------- Comparison ----------------

print("\n\nCOMPARISON OF GENERATED POSTS")
print("="*60)

print("""
Prompt Type     Creativity     Engagement     Structure     Completeness

Zero-shot       Good           Moderate       Basic         Good

One-shot        Better         Good           Organized     Very Good

Few-shot        Highest        Highest        Excellent     Highest


Conclusion:
Few-shot prompting generates the most effective promotional post because
examples help the model understand the required style, format, and marketing
elements.
""")
