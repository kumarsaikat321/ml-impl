import random


class DataGenerator:

    def __init__(self, n=100, d=1, mean=0.0, std=1.0):
        self.n = n  # number of data points
        self.d = d  # number of dimension
        self.mean = mean  # agg mean of data
        self.std = std  # agg std of data

    def generate(self):
        # write your function here
        output = []
        for i in range(self.d):
            output.append([random.random()] * self.n)

        return output
