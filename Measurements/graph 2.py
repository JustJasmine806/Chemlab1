#This is the code for Graph 2 (Density of water with a volumetric pipette)
import matplotlib.pyplot as plt
import numpy as np

# Density data from the five trials
trials = ["Trial 1", "Trial 2", "Trial 3", "Trial 4", "Trial 5"]
densities = [0.997, 0.992, 0.994, 0.996, 0.995]

# Calculate the average density
average_density = np.mean(densities)

# True density of water at 23.5°C
true_density = 0.9975

# Create the bar graph
plt.figure(figsize=(10, 6))

plt.bar(
    trials,
    densities,
    color="skyblue",
    edgecolor="black",
    label="Measured Density"
)

# Add average density line
plt.axhline(
    average_density,
    color="red",
    linestyle="--",
    linewidth=2,
    label=f"Average Density = {average_density:.4f} g/mL"
)

# Add true density line
plt.axhline(
    true_density,
    color="green",
    linestyle="-",
    linewidth=2,
    label=f"True Density = {true_density:.4f} g/mL"
)

# Labels and title
plt.xlabel("Trial")
plt.ylabel("Density (g/mL)")
plt.title("Density of Water Using a Volumetric Pipette at 23.2°C")

# Set y-axis range to make the differences visible
plt.ylim(0.99, 1.00)

# Add grid
plt.grid(axis="y", linestyle=":", alpha=0.5)

# Add legend
plt.legend()

# Display the graph
plt.tight_layout()
plt.show()