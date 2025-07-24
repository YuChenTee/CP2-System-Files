# 📡 RL-Based SBS Optimization in NS-3 with ns3-gym

This project implements a reinforcement learning framework for optimizing Small Base Station (SBS) operations in ultra-dense small cell networks (UDSCNs). It combines the NS-3 simulator and the `ns3-gym` interface to create an interactive RL environment for training and testing DDQN and PPO agents.

> 🖥 **Note:** This project is intended to be run in a **Windows Subsystem for Linux (WSL)** environment **with NS-3 and ns3-gym properly installed**.

---

## 📂 Project Structure

| File                          | Description                                                                                                                                                                                                          |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ns3-gym_test.cc`             | The C++ simulation file that defines the SBS network environment using NS-3. It includes environment setup, handover logic, and reward computation.                                                                  |
| `DDQN_Training_ns3gym.py`     | The main training script using a Double Deep Q-Network (DDQN) agent. It launches the NS-3 environment as a subprocess and communicates via `ns3-gym`. Neural network hyperparameters can be configured in this file. |
| `PPO_Training.py`             | The training script for a Proximal Policy Optimization (PPO) agent. Similar to the DDQN script, it allows hyperparameter tuning and interacts with NS-3.                                                             |
| `comparison-test.py`          | Testing script that loads trained DDQN and PPO models and compares them against a baseline over 50 randomized network scenarios. Outputs performance comparison plots.                                               |
| `episode_metrics.csv`         | A CSV file containing training episode reward metrics for further statistical analysis.                                                                                                                              |
| `data_clealiness_analysis.py` | Script that analyzes `episode_metrics.csv` and visualizes reward distributions using boxplots to detect outliers.                                                                                                    |

---

## 🚀 Getting Started

1. **Set up WSL (Windows Subsystem for Linux)** with Ubuntu or another Linux distribution.

2. **Install NS-3** and ensure `ns3-gym` is correctly integrated.

3. **Clone this repository** and navigate to the root folder.

4. **Build the NS-3 project** (from the NS-3 directory):

5. **Train the RL agent**

6. **Run comparison tests**

7. **Analyze training data**

---

## 📌 Notes

* Ensure proper socket communication between Python and NS-3 (port conflicts may cause failures).
* For reproducibility, random seeds are set inside the training scripts.

---
