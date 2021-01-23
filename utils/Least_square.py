import numpy as np
import random


class least_sq:
    def __init__(self, x, y, ite=100, lr=0.001):

        self.x = x
        self.y = y
        self.ite = ite
        self.w = random.random()
        self.b = random.random()
        self.lr = lr

    def least_square(self):
        l_s = 0
        for i in range(len(self.x)):
            l_s += np.square((self.y[i] - self.w * self.x[i] - self.b))
        return l_s / len(self.x)

    def update_w(self):
        for i in range(len(self.x)):
            p = 0
            p += (-1 * (2 * self.x[i] * (self.y[i] - self.w * self.x[i] - self.b)))
        return p / len(self.x)

    def update_b(self):
        for i in range(len(self.x)):
            p = 0
            p += (-1 * (2 * (self.y[i] - self.w * self.x[i] - self.b)))
        return p / len(self.x)

    def fit(self):
        for j in range(self.ite):
            self.w -= self.update_w() * self.lr
            self.b -= self.update_b() * self.lr

        return self.w, self.b
