import re
import pandas as pd

# Updated log from user
# Replace 'your_file.txt' with the path to your text file
with open('log/output.txt', 'r', encoding='utf-8') as file:
    log_text = file.read()

# Parse the latency values
pattern = re.compile(r'System Latency: ([\d.]+) ms\. FC Latency: ([\d.]+), Vicon Latency: ([\d.]+)')
matches = pattern.findall(log_text)

# Convert to DataFrame
df = pd.DataFrame(matches, columns=["System Latency", "FC Latency", "Vicon Latency"]).astype(float)

# Calculate min, max, and average
summary = {
    "Latency Type": ["System Latency", "FC Latency", "Vicon Latency"],
    "Min (ms)": [df[col].min() for col in df.columns],
    "Max (ms)": [df[col].max() for col in df.columns],
    "Avg (ms)": [df[col].mean() for col in df.columns],
}

print(summary)

