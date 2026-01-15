Here is the `README.md` file in polished English, suitable for sharing with a wider audience, such as researchers and developers.

---

# RSDTS: Regret-Optimal and Stable Distributed Task Scheduling

## Project Overview

RSDTS (Regret-Optimal and Stable Distributed Task Scheduling) is a distributed task scheduling algorithm designed for **Ubiquitous Operating Systems** (UOS). It combines **mean-field control** and **online optimization** methods to provide a scalable, efficient, and stable scheduling solution in environments with highly dynamic and heterogeneous nodes.

* **Efficiency**: By utilizing mean-field control, RSDTS minimizes regret while maintaining task scheduling in large-scale, distributed systems.
* **Stability**: The Lyapunov drift-plus-penalty method is applied to ensure queue stability and provide bounds on task delays.
* **Scalability**: The algorithm is designed to handle large numbers of nodes while maintaining low computational overhead.

## Features

* **Distributed Task Scheduling**: The algorithm operates in a fully decentralized manner, where each node makes its own scheduling decisions, making it suitable for large-scale distributed systems.
* **Dynamic Environment Adaptation**: RSDTS adapts to system dynamics and node churn using online optimization and mean-field modeling.
* **Stability and Delay Guarantees**: The algorithm provides theoretical guarantees for queue stability and task delay bounds.
* **Scalability**: RSDTS maintains high performance even as the system scales to thousands or even millions of nodes.

## Installation & Dependencies

### Prerequisites

This project is built in Python 3.x and uses the `numpy` library.

```bash
pip install numpy
```

### Cloning the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/rsdts.git
cd rsdts
```

### Configuration & Running

The experimental parameters, such as the number of nodes, task arrival rate, and maximum simulation time, can be configured in the `config/settings.py` file.

```python
NUM_NODES = 100         # Number of nodes in the system
TASK_LAMBDA = 10        # Task arrival rate per node
MAX_TIME_SLOTS = 10000  # Maximum simulation time steps
CHURN_RATE = 0.1        # Node churn rate
V = 20                  # Control parameter balancing regret and delay
```

Run the simulation by executing the `main.py` script:

```bash
python main.py
```

The script will output the total regret, total delay, and execution time of the simulation.

## Experiment Setup

The project comes with predefined experimental setups. Below are the key parameters used for evaluation:

* **Objective**: Evaluate the performance of RSDTS under different system loads, node scales, and task arrival rates.
* **Comparison**: Compare RSDTS with other state-of-the-art distributed scheduling algorithms, such as D-Lyapunov, MARL, and Greedy-LB.
* **Metrics**: Key performance metrics include **regret**, **task delay**, and **queue stability**.

You can modify the `main.py` script to adjust simulation time and the number of nodes according to your experimental needs.

## Code Structure

* **core/**: Contains the main scheduling logic, node model, and utility functions.

  * `scheduler.py`: Implements the core scheduling algorithm for RSDTS.
  * `node.py`: Defines the node attributes and initialization methods.
  * `utils.py`: Contains auxiliary functions for computing regret, delay, and task distribution.
* **config/**: Configuration files for system parameters and experiment settings.

  * `settings.py`: Stores system and experiment parameters.
* **main.py**: Main program entry point that runs the scheduling simulation and outputs the results.

## Example Usage

Here’s an example of how to run the simulation:

```python
from core.scheduler import RSDTS
from config.settings import NUM_NODES, TASK_LAMBDA, MAX_TIME_SLOTS, CHURN_RATE, V

def main():
    scheduler = RSDTS(num_nodes=NUM_NODES, task_lambda=TASK_LAMBDA, max_time_slots=MAX_TIME_SLOTS, churn_rate=CHURN_RATE, V=V)
    total_regret, total_delay = scheduler.simulate()
    
    print(f"Total Regret: {total_regret}")
    print(f"Total Delay: {total_delay}")

if __name__ == "__main__":
    main()
```

### Sample Output

```bash
Time slot 1000, Regret: 1020, Average Delay: 23.5
Time slot 2000, Regret: 2040, Average Delay: 24.7
Time slot 10000, Regret: 3820, Average Delay: 45.8
Total Regret: 3820
Total Delay: 102450.0
Time taken: 12.54 seconds
```

## Experimental Results

In our experiments, RSDTS has demonstrated superior performance under various load conditions, node scales, and node churn.

* **Sublinear Regret**: The regret growth of RSDTS is sublinear, indicating the algorithm performs well even over long-term operation.
* **Queue Stability**: RSDTS maintains stable queue lengths even under high system load.
* **Delay Optimization**: By adjusting the control parameter `V`, RSDTS successfully optimizes task delays.

For more detailed results and analysis, refer to the `Results and Analysis` section.

## Contributing

We welcome contributions to this project! If you have any improvements, bug fixes, or new features to add, please follow the steps below to contribute:

1. Fork the repository.
2. Create a new branch for your changes.
3. Submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
