import matplotlib.pyplot as plt
import numpy as np

# Hypothetical data for plotting
requests = np.arange(1, 11)  # 10 requests
response_time_original = np.random.uniform(0.8, 1.2, size=10)  # Original response times
response_time_enhanced = np.random.uniform(0.4, 0.6, size=10)  # Enhanced response times

# Plotting response times
plt.figure(figsize=(10, 5))
plt.plot(requests, response_time_original, label='Original GFS', marker='o')
plt.plot(requests, response_time_enhanced, label='Enhanced GFS', marker='x')
plt.xlabel('Request Number')
plt.ylabel('Response Time (seconds)')
plt.title('Response Time Comparison: Original GFS vs. Enhanced GFS')
plt.legend()
plt.grid(True)
plt.show()

# Hypothetical availability data
days = np.arange(1, 11)  # 10 days
availability_original = np.random.uniform(90, 95, size=10)  # Original availability
availability_enhanced = np.random.uniform(98, 100, size=10)  # Enhanced availability

# Plotting system availability
plt.figure(figsize=(10, 5))
plt.plot(days, availability_original, label='Original GFS', marker='o')
plt.plot(days, availability_enhanced, label='Enhanced GFS', marker='x')
plt.xlabel('Day')
plt.ylabel('System Availability (%)')
plt.title('System Availability Comparison: Original GFS vs. Enhanced GFS')
plt.legend()
plt.grid(True)
plt.show()
