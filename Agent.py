
import numpy as np
np.random.seed(314)

class Agent:
    def __init__(self, epsilon, n_arms=10):
        self.epsilon = epsilon                  # Epsilon value for epsilon-greedy strategy
        self.n_arms = n_arms                    # Number of arms
        self.rewards = np.zeros(n_arms)         # Matrix to store the estimated rewards for each arm
        self.pull_count = np.zeros(n_arms)      # Matrix to store the number of times each arm was pulled

    def select_arm(self):
        # Exploration
        if np.random.random() < self.epsilon: 
            return np.random.randint(self.n_arms)

        # Exploitation
        else:
            return np.argmax(self.rewards)

    def update_estimates(self, arm, reward):
        
        # Updating the number of times the arm was pulled
        self.pull_count[arm] += 1

        # Updating the estimated rewards for the arm
        # ------------------------------------------- #
        # Variables:
        n = self.pull_count[arm]
        Qn = self.rewards[arm]

        # Formula: Q_(n+1) = Q_n + 1/n * [R_n - Q_n]
        self.rewards[arm] += (1/n) * (reward - Qn)