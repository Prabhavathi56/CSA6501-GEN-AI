# Zero-shot Prompt
zero_shot = """
Write a product description for a Smart Fitness Watch.
Highlight its key features, health tracking capabilities,
battery life, and stylish design in about 100 words.
"""

zero_output = """
Stay connected and achieve your fitness goals with the Smart Fitness Watch.
It features heart rate monitoring, blood oxygen tracking, sleep analysis,
step counting, and multiple sports modes. Receive call and message
notifications directly on your wrist while enjoying up to 10 days of battery
life. Its lightweight, water-resistant, and stylish design makes it perfect
for workouts, office use, and everyday wear.
"""

# One-shot Prompt
one_shot = """
Example:

Product: Wireless Bluetooth Earbuds

Description:
Experience crystal-clear sound with Wireless Bluetooth Earbuds.
Featuring noise cancellation, long battery life, fast charging,
and a comfortable ergonomic design.

Now generate a product description for:

Product: Smart Fitness Watch
"""

one_output = """
The Smart Fitness Watch helps you stay fit and connected with advanced health
tracking features such as heart rate monitoring, sleep tracking, blood oxygen
measurement, and multiple sports modes. Its sleek design, water resistance,
and long-lasting battery make it ideal for daily use.
"""

# Few-shot Prompt
few_shot = """
Example 1:
Product: Wireless Bluetooth Earbuds
Description: Noise cancellation, long battery life, Bluetooth connectivity.

Example 2:
Product: Smart Water Bottle
Description: Tracks water intake and reminds you to stay hydrated.

Now generate a product description for:
Product: Smart Fitness Watch
"""

few_output = """
Experience smarter fitness with the Smart Fitness Watch. It monitors heart
rate, SpO₂, sleep, calories burned, and daily activity. Enjoy smart
notifications, multiple workout modes, up to 10 days of battery life, and a
modern water-resistant design suitable for fitness and everyday wear.
"""

print("========== ZERO-SHOT ==========")
print("Prompt:")
print(zero_shot)
print("Output:")
print(zero_output)

print("\n========== ONE-SHOT ==========")
print("Prompt:")
print(one_shot)
print("Output:")
print(one_output)

print("\n========== FEW-SHOT ==========")
print("Prompt:")
print(few_shot)
print("Output:")
print(few_output)
