import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd

# Load and clean data
data = pd.read_csv('Depth Data.csv')
data['Point'] = pd.to_numeric(data['Point'], errors='coerce')
data['Depth (m)'] = pd.to_numeric(data['Depth (m)'], errors='coerce')
data = data.dropna(subset=['Point', 'Depth (m)']).reset_index(drop=True)
for i in range(1, len(data)):
    prev_val = data.loc[i - 1, 'Depth (m)']
    curr_val = data.loc[i, 'Depth (m)']
    
    if abs(curr_val - prev_val) >= 50:

        start_idx = max(0, i - 2)
        data.loc[i, 'Depth (m)'] = data.loc[start_idx:i - 1, 'Depth (m)'].mean()

fig, ax = plt.subplots()

# 1. Line color set to navy blue (change color name or hex code as desired)
(line,) = ax.plot([], [], color="navy", lw=2)

# 2. Fixed Y-axis limits and tick labels (from -400 to 0 every 20m for readability)
y_ticks = np.arange(-450, 1, 20)
ax.set_yticks(y_ticks)
ax.set_yticklabels([f"{tick}m" for tick in y_ticks])  # Adds 'm' suffix to labels
ax.set_ylim(-450, 0)
ax.set_xlim(data['Point'].min(), data['Point'].max())

# Axis titles
ax.set_xlabel("Point")
ax.set_ylabel("Depth (m)")
ax.set_title("Live Depth Animation")

def animate(i):
    x_vals = data['Point'].iloc[:i+1]
    y_vals = data['Depth (m)'].iloc[:i+1]
    line.set_data(x_vals, y_vals)
    return(line,)

ani = FuncAnimation(fig, animate, frames=len(data),interval=1000)

plt.tight_layout()
plt.show()
