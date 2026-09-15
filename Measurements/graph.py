#This code produces the bar graph for the measurements lab
#This is the code for Graph 2 (Density of water with a Graduated cylinder)
import matplotlib.pyplot as plt
import numpy as np

# Data
trials = ["Trial 1", "Trial 2", "Trial 3", "Trial 4", "Trial 5"]
densities = [0.947, 0.978, 0.993, 0.991, 0.985]

# Calculate average
average_density = np.mean(densities)

# True density of water at 23.5°C
true_density = 0.9975

# Create bar graph
plt.figure(figsize=(10, 6))

plt.bar(
    trials,
    densities,
    color="skyblue",
    edgecolor="black",
    label="Measured Density"
)

# Average line
plt.axhline(
    average_density,
    color="red",
    linestyle="--",
    linewidth=2,
    label=f"Average Density = {average_density:.4f} g/mL"
)

# True density line
plt.axhline(
    true_density,
    color="green",
    linestyle="-",
    linewidth=2,
    label=f"True Density = {true_density:.4f} g/mL"
)

# Labels
plt.xlabel("Trial")
plt.ylabel("Density (g/mL)")
plt.title("Density of Water at 23.5°C Using Graduate Cylinder")

# Make the differences easier to see
plt.ylim(0.94, 1.00)

# Grid
plt.grid(axis="y", linestyle=":", alpha=0.5)

# Legend
plt.legend()

# Display graph
plt.tight_layout()
plt.show()