# Task 1--> API Intergration and Data Visulization for CodTech python internship. 
# Instruction: 
#     # Use python to fetch data from a public API(E.G. OPENWEATHERMAP) and create visulizations using MATPLOTLIB or SEABORN.
# Deliverable:
#     A scrip and a visulization dashboard
# Using MatPlotLib for the graph visualization


import matplotlib.pyplot as plt
import requests
from datetime import datetime
import numpy as np

# Setup API by creating a free OpenWeatherMap account and going to API keys
API_KEY = '48b54254645f64343c9b7e04995995fd'
city = 'Pune'
url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

if data.get('cod') != '200':
    print("API Error:", data.get('message', 'Unknown error'))
    exit()

#  Extract the data to show on the graph
temperatures = []
timestamps = []

for entry in data['list']:
    temperatures.append(entry['main']['temp'])
    timestamps.append(datetime.strptime(entry['dt_txt'], "%Y-%m-%d %H:%M:%S"))

# Using temperature coloring to show higher temperature in Red and lower temperature in blue color
norm = plt.Normalize(min(temperatures), max(temperatures))
colors = plt.cm.coolwarm(norm(temperatures))

# Create plot and axis 
fig, ax = plt.subplots(figsize=(14, 6))

# Scatter plot with colors
scatter = ax.scatter(timestamps, temperatures, c=colors, s=80, edgecolors='black')
ax.plot(timestamps, temperatures, color='gray', linewidth=1.5, alpha=0.4)

# Giving the titles and labels for better understanding
ax.set_title(f"Temperature Forecast for {city}", fontsize=18, fontweight='bold')
ax.set_xlabel("Date & Time", fontsize=14, labelpad=15)
ax.set_ylabel("Temperature (°C)", fontsize=14, labelpad=10)
ax.grid(True, linestyle='--', alpha=0.5)

# Adding the colorbar to the figure
sm = plt.cm.ScalarMappable(cmap='coolwarm', norm=norm)
sm.set_array([])  # Required for ScalarMappable
fig.colorbar(sm, ax=ax, label="Temperature Scale (°C)")

# Visualizing the graph
plt.tight_layout()
plt.show()
