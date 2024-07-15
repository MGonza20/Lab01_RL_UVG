
import numpy as np

class Bandit:
    def __init__(self, n_arms=10):
        self.n_arms = n_arms
        self.arms_probabilities = np.random.rand(n_arms)
        
    def pull(self, arm): 
        random_number = np.random.rand()
        arm_prob = self.arms_probabilities[arm]

        if random_number < arm_prob: return 1 
        else: return 0