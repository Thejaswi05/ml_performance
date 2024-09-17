import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Load the data into a DataFrame
data = pd.read_csv('./sample_jtls/results.jtl')

# Convert timeStamp from milliseconds to a readable datetime format
data['timeStamp'] = pd.to_datetime(data['timeStamp'], unit='ms')

# Create a figure and set of subplots
plt.figure(figsize=(12, 8))

# Plot Elapsed Time
plt.subplot(3, 1, 1)
plt.plot(data['timeStamp'], data['elapsed'], label='Elapsed Time (ms)', color='blue')
plt.ylabel('Elapsed Time (ms)')
plt.title('Performance Test Results Over Time')
plt.grid(True)

# Plot Latency
plt.subplot(3, 1, 2)
plt.plot(data['timeStamp'], data['Latency'], label='Latency (ms)', color='green')
plt.ylabel('Latency (ms)')
plt.grid(True)

# Plot Response Size
plt.subplot(3, 1, 3)
plt.plot(data['timeStamp'], data['bytes'], label='Response Size (bytes)', color='red')
plt.ylabel('Response Size (bytes)')
plt.xlabel('Time')
plt.grid(True)

# Improve layout and display the plot
plt.tight_layout()
plt.show()
