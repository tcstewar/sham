import numpy as np

def sample_to_sum(rng, target, sd, count):
    s = rng.randn(count) * sd / np.sqrt(count)
    s += (target - sum(s)) / count
    return s
