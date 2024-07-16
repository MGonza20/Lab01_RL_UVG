
import numpy as np
np.random.seed(314)

class Bandit:
    def __init__(self, n_arms=10):
        self.n_arms = n_arms
        self.arms_probs = np.random.rand(n_arms)
        
    def pull(self, arm): 
        random_number = np.random.random()
        arm_prob = self.arms_probs[arm]

        if random_number < arm_prob: 
            return 1 
        else: 
            return 0