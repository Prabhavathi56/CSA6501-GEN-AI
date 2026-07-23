# Experiment: Zero-shot, One-shot, and Few-shot Prompting
# Task: Generate a professional email requesting leave due to illness


# ---------------- Zero-shot Prompt ----------------

zero_shot_prompt = """
Write a professional email requesting leave due to illness.
Include a subject, greeting, reason for leave, leave duration,
and a polite closing.
"""

zero_shot_output = """
Subject: Request for Sick Leave

Dear Manager,

I am writing to request leave as I am feeling unwell and unable
to attend work. I need some time to recover and take proper rest.
Kindly grant me leave for two days from 24th July to 25th July.

I will complete any pending tasks after I return and ensure a
smooth workflow. I apologize for any inconvenience caused and
request your understanding.

Thank you for your consideration.

Sincerely,
Employee
"""


# ---------------- One-shot Prompt ----------------

one_shot_prompt = """
Example:

Subject: Request for Leave Due to Personal Reasons

Dear Sir/Madam,

I would like to request leave for one day due to an unavoidable
personal reason. I kindly request you to approve my leave.
I will ensure that my pending responsibilities are completed.

Thank you for your support.

Regards,
John

Now generate a professional email requesting leave due to illness.
"""

one_shot_output = """
Subject: Request for Sick Leave Due to Illness

Dear Sir/Madam,

I am writing to inform you that I am suffering from illness and
will not be able to attend work for the next two days. Therefore,
I kindly request you to grant me sick leave from 24th July to
25th July.

I will take the necessary rest and resume my duties as soon as
I recover. I will also ensure that any pending work is managed
properly.

I kindly request your approval and understanding.

Thank you.

Regards,
Employee
"""


# ---------------- Few-shot Prompt ----------------

few_shot_prompt = """
Example 1:

Subject: Request for Medical Leave

Dear Manager,

I am feeling unwell and need medical rest. Kindly approve my
leave request for two days. I will complete pending tasks after
returning.

Regards,
Employee


Example 2:

Subject: Sick Leave Application

Dear Team Lead,

Due to health issues, I am unable to attend work today.
I request you to grant me leave and apologize for any
inconvenience caused.

Thank you.

Now generate a professional email requesting leave due to illness.
"""

few_shot_output = """
Subject: Request for Sick Leave Due to Health Issues

Dear Manager,

I hope you are doing well. I am writing this email to inform you
that I am currently suffering from illness and have been advised
to take rest. Therefore, I kindly request you to grant me sick
leave for two days from 24th July to 25th July.

I will make sure that all important tasks are completed after
my recovery. I appreciate your understanding and support during
this time.

Kindly approve my leave request.

Thank you.

Sincerely,
Employee
"""


# ---------------- Display Results ----------------

print("="*60)
print("ZERO-SHOT EMAIL")
print("="*60)
print(zero_shot_output)


print("\n"+"="*60)
print("ONE-SHOT EMAIL")
print("="*60)
print(one_shot_output)


print("\n"+"="*60)
print("FEW-SHOT EMAIL")
print("="*60)
print(few_shot_output)


# ---------------- Comparison ----------------

print("\n\nCOMPARISON OF GENERATED EMAILS")
print("="*60)

print("""
Prompt Type     Tone          Grammar       Formatting      Completeness

Zero-shot       Good          Good          Basic           Moderate

One-shot        Professional  Very Good     Good            Good

Few-shot        Formal        Excellent     Well-structured Highest


Conclusion:
Few-shot prompting generates the most professional email because examples
help the model understand the correct tone, structure, and required details.
""")
