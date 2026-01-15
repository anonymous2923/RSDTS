import numpy as np
from .node import Node
from .utils import compute_regret, compute_delay, mean_field_control


class RSDTS:
    def __init__(self, num_nodes, task_lambda, max_time_slots=10000, churn_rate=0.1, V=20):
        self.num_nodes = num_nodes
        self.max_time_slots = max_time_slots
        self.task_lambda = task_lambda  # Task arrival rate
        self.V = V  # Control parameter
        self.churn_rate = churn_rate  # Node churn rate

        # Initialize nodes
        self.nodes = [Node() for _ in range(self.num_nodes)]

        # Initialize state variables
        self.task_queue = np.zeros(self.num_nodes)  # Task queue for each node
        self.task_load = np.zeros(self.num_nodes)  # Task load for each node

    def _simulate_task_arrival(self, t):
        """Simulate task arrivals using Poisson process."""
        task_arrival = np.random.poisson(self.task_lambda)
        for i in range(self.num_nodes):
            self.task_queue[i] += task_arrival

    def _update_system_state(self):
        """Simulate system churn (node join/leave)."""
        churn_count = int(self.churn_rate * self.num_nodes)
        for i in np.random.choice(self.num_nodes, churn_count, replace=False):
            self.nodes[i] = Node()  # New node
            self.task_queue[i] = 0  # Reset task queue for churned node

    def _distribute_tasks(self):
        """Distribute tasks using mean-field control approach."""
        avg_queue = np.mean(self.task_queue)
        for i in range(self.num_nodes):
            self.task_load[i] = mean_field_control(self.task_queue[i], self.nodes[i], avg_queue)
            self.task_queue[i] = max(0, self.task_queue[i] - self.task_load[i])

    def simulate(self):
        total_regret = 0
        total_delay = 0

        for t in range(self.max_time_slots):
            # Simulate task arrival and system churn
            self._simulate_task_arrival(t)
            self._update_system_state()

            # Distribute tasks
            self._distribute_tasks()

            # Compute regret and delay
            optimal_task_load = np.sum(self.task_queue)
            regret = compute_regret(self.task_load, optimal_task_load)
            delay = compute_delay(self.task_queue)

            total_regret += regret
            total_delay += delay

        return total_regret, total_delay
