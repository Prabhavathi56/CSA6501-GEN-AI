# Experiment: Zero-shot, One-shot, and Few-shot Prompting
# Topic: Applications of Artificial Intelligence in Healthcare

# ---------------- Zero-shot ----------------

zero_prompt = """
Write a 200-word blog on 'Applications of Artificial Intelligence in Healthcare.'
"""

zero_output = """
Artificial Intelligence (AI) is transforming the healthcare industry by improving the accuracy, speed, and efficiency of medical services. AI-powered systems help doctors diagnose diseases such as cancer, diabetes, and heart conditions at an early stage using medical images and patient data. Virtual health assistants provide medical guidance, schedule appointments, and remind patients to take medications. AI also supports robotic surgeries, making procedures more precise and reducing recovery time. Hospitals use AI to manage patient records, predict disease outbreaks, and improve resource allocation. Wearable devices with AI monitor heart rate, blood pressure, sleep patterns, and physical activity in real time. Researchers use AI to discover new medicines and develop vaccines faster by analyzing large amounts of medical data. AI improves personalized treatment plans by studying each patient's health history and lifestyle. Although AI cannot replace doctors, it acts as a powerful tool to support better decision-making and improve patient care. As technology continues to advance, AI will play an even greater role in making healthcare more accessible, affordable, and effective for people around the world.
"""

# ---------------- One-shot ----------------

one_prompt = """
Example:

Topic: Benefits of Online Education

Blog:
Online education has changed the way students learn. It provides flexibility,
easy access to learning materials, and allows students to attend classes from
any location. Digital platforms improve learning through videos, quizzes, and
interactive sessions.

Now write a 200-word blog on:
'Applications of Artificial Intelligence in Healthcare.'
"""

one_output = """
Artificial Intelligence (AI) has become an important technology in modern healthcare. It helps doctors detect diseases quickly and accurately using medical imaging and patient data analysis. AI-powered chatbots provide health information and assist patients with appointment scheduling. Hospitals use AI to manage medical records, predict patient admissions, and improve overall efficiency. Robotic systems assist surgeons in performing complex operations with greater precision. AI also supports personalized medicine by recommending treatments based on a patient's medical history. Wearable health devices continuously monitor vital signs and alert users about possible health issues. Researchers use AI to speed up drug discovery and vaccine development by analyzing large datasets. AI reduces human errors, saves time, and improves patient outcomes. While human doctors remain essential, AI acts as a valuable assistant that enhances healthcare services. As AI technology continues to grow, it will make healthcare smarter, faster, and more accessible for everyone.
"""

# ---------------- Few-shot ----------------

few_prompt = """
Example 1:

Topic: Importance of Renewable Energy

Blog:
Renewable energy helps reduce pollution and protects the environment.
Solar and wind energy are clean and sustainable sources of power.

Example 2:

Topic: Role of Cloud Computing

Blog:
Cloud computing provides online storage, improves collaboration,
and reduces infrastructure costs for businesses.

Now write a 200-word blog on:
'Applications of Artificial Intelligence in Healthcare.'
"""

few_output = """
Artificial Intelligence (AI) is revolutionizing healthcare by improving medical diagnosis, treatment, and patient care. AI systems analyze medical images to detect diseases such as cancer, pneumonia, and heart disorders with high accuracy. Virtual assistants help patients book appointments, answer health-related questions, and provide medication reminders. AI-powered wearable devices monitor heart rate, blood pressure, oxygen levels, and sleep quality, helping users maintain better health. Hospitals use AI to manage patient records, optimize staff scheduling, and predict disease outbreaks. AI also supports robotic surgery, allowing doctors to perform complex procedures with greater precision and fewer complications. In medical research, AI accelerates drug discovery by analyzing vast amounts of biological data. Personalized treatment plans can be created using AI by studying each patient's medical history and genetic information. Although AI cannot replace healthcare professionals, it serves as an intelligent assistant that improves efficiency and decision-making. As technology continues to advance, AI will play a significant role in creating a smarter, more accessible, and higher-quality healthcare system for people worldwide.
"""

print("=" * 60)
print("ZERO-SHOT PROMPT")
print("=" * 60)
print(zero_prompt)
print("Generated Blog:")
print(zero_output)

print("\n" + "=" * 60)
print("ONE-SHOT PROMPT")
print("=" * 60)
print(one_prompt)
print("Generated Blog:")
print(one_output)

print("\n" + "=" * 60)
print("FEW-SHOT PROMPT")
print("=" * 60)
print(few_prompt)
print("Generated Blog:")
print(few_output)
