import csv
import matplotlib.pyplot as plt

# File path
csv_file = "episode_metrics.csv"

# Initialize lists
episode, total_reward, avg_power, avg_qos, avg_prb, epsilon = [], [], [], [], [], []

# Read data manually
with open(csv_file, newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        episode.append(int(row["episode"]))
        total_reward.append(float(row["total_reward"]))
        avg_power.append(float(row["avg_power"]))
        avg_qos.append(float(row["avg_qos"]))
        avg_prb.append(float(row["avg_prb"]))
        epsilon.append(float(row["epsilon"]))

# Prepare data
data = [total_reward, avg_power, avg_qos, avg_prb, epsilon]
labels = ["Total Reward", "Avg Power", "Avg QoS", "Avg PRB", "Epsilon"]
valid_ranges = [(-100, 100), (-1, 1), (-1, 1), (-1, 1), (0.05, 1.0)]

# Plot
plt.figure(figsize=(14, 6))
for i in range(len(data)):
    plt.subplot(1, 5, i + 1)
    plt.boxplot(data[i], vert=True, patch_artist=True)
    plt.axhline(valid_ranges[i][0], color='red', linestyle='--', linewidth=1)
    plt.axhline(valid_ranges[i][1], color='green', linestyle='--', linewidth=1)
    plt.title(labels[i])
    plt.ylim(valid_ranges[i][0] - 0.1, valid_ranges[i][1] + 0.1)

plt.suptitle("Boxplot of Metrics with Valid Range Indicators")
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("basic_boxplot_clean.png")
plt.close()

print("✅ Boxplot saved as 'basic_boxplot_clean.png'")