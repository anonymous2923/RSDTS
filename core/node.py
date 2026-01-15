import numpy as np

class Node:
    def __init__(self):
        self.mu = np.random.uniform(0.5, 2.0)  # Random computational power
        self.energy = np.random.uniform(0.1, 0.5)  # Random energy model
        self.latency = np.random.uniform(0.01, 0.1)  # Random latency

    def __str__(self):
        return f"Node(mu={self.mu}, energy={self.energy}, latency={self.latency})"
