
import numpy as np

class Agent:
    def __init__(self, epsilon, n_arms=10):
        self.epsilon = epsilon                  # Epsilon value for epsilon-greedy strategy / exploration 
        self.n_arms = n_arms                    # Number of arms
        self.rewards = np.zeros(n_arms)         # Matrix to store the estimated rewards for each arm
        self.pull_count = np.zeros(n_arms)      # Matrix to store the number of times each arm was pulled

    def select_arm(self):
        # Exploration
        if np.random.rand() < self.epsilon: return np.random.randint(self.n_arms)

        # Exploitation
        else: return np.argmax(self.rewards)

