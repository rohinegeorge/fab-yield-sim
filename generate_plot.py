import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.plot([1, 2, 3, 4, 5], [82, 85, 84, 88, 86.4], label="Simulated Wafer Yield (%)", color="#1f77b4")
plt.axhline(y=86.4, color="r", linestyle="--", label="Mean Target Yield (86.4%)")
plt.title("Silicon Fab Yield Dynamics & Defect Clustering")
plt.xlabel("Wafer Batch Run")
plt.ylabel("Pass Rate (%)")
plt.legend()
plt.tight_layout()
plt.savefig("assets/yield_plot.png")
print("Plot saved to assets/yield_plot.png")
