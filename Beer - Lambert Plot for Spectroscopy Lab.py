# This code produces the Beer graph for the spectroscopy lab

import numpy as np
import matplotlib.pyplot as plt

# Calcium concentration (ppm)
concentration = np.array([2, 4, 6, 8, 10, 15])

# Recorded absorbance
absorbance = np.array([
    0.064, 0.117, 0.117,
    0.240, 0.302, 0.440
])

# Linear regression
slope, intercept = np.polyfit(
    concentration, absorbance, 1
)

predicted = slope * concentration + intercept

r_squared = 1 - (
    np.sum((absorbance - predicted)**2) /
    np.sum((absorbance - np.mean(absorbance))**2)
)

# Plot
x_line = np.linspace(0, 16, 200)
y_line = slope * x_line + intercept

plt.scatter(
    concentration, absorbance,
    color="blue", label="Calcium Standards"
)

plt.plot(
    x_line, y_line,
    color="red", label="Linear Regression"
)

plt.xlabel("Calcium Concentration (ppm)")
plt.ylabel("Absorbance (unitless)")
plt.title("Beer-Lambert Calibration Curve for Calcium")

equation = (
    f"A = {slope:.8f}C {intercept:+.8f}\n"
    f"R² = {r_squared:.4f}"
)

plt.text(
    0.05, 0.95, equation,
    transform=plt.gca().transAxes,
    verticalalignment="top",
    bbox=dict(facecolor="white", alpha=0.8)
)

plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()