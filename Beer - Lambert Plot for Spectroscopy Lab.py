# This code produces the Beer graph for the spectroscopy lab

import numpy as np
import matplotlib.pyplot as plt

# Calcium concentrations (ppm)
concentration = np.array([2, 4, 6, 8, 10, 15])

# Absorbance values from the lab notebook
absorbance = np.array([0.064, 0.117, 0.177, 0.240, 0.302, 0.440])

# Unknown sample absorbance
unknown_absorbance = 0.125

# Calculate linear regression
slope, intercept = np.polyfit(concentration, absorbance, 1)

# Calculate predicted absorbance
predicted = slope * concentration + intercept

# Calculate R-squared
ss_res = np.sum((absorbance - predicted) ** 2)
ss_tot = np.sum((absorbance - np.mean(absorbance)) ** 2)
r_squared = 1 - (ss_res / ss_tot)

# Calculate unknown concentration
unknown_concentration = (unknown_absorbance - intercept) / slope

# Generate line of best fit
x_line = np.linspace(0, 16, 100)
y_line = slope * x_line + intercept

# Create graph
plt.figure(figsize=(9, 6))

# Plot experimental data
plt.scatter(concentration, absorbance,
            color="blue", s=70,
            label="Calcium Standards")

# Plot line of best fit
plt.plot(x_line, y_line,
         color="red",
         label="Linear Regression")

# Equation and R-squared
equation = f"Absorbance = {slope:.5f}(Concentration) + {intercept:.5f}"
r2_text = f"R² = {r_squared:.4f}"

plt.text(0.05, 0.95,
         equation + "\n" + r2_text,
         transform=plt.gca().transAxes,
         fontsize=10,
         verticalalignment="top",
         bbox=dict(facecolor="white", alpha=0.8))

# Graph formatting
plt.xlabel("Calcium Concentration (ppm)")
plt.ylabel("Absorbance (unitless)")
plt.title("Beer-Lambert Calibration Curve for Calcium")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()

# Save graph
plt.savefig("Calcium_Calibration_Curve.png", dpi=300)

# Display graph
plt.show()

# Print results
print("Calibration Equation:", equation)
print(r2_text)
print(f"Unknown Absorbance: {unknown_absorbance}")
print(f"Unknown Calcium Concentration: {unknown_concentration:.3f} ppm")