import numpy as np
import random

class least_sq:
    def __init__(self, x, y, m, b,l_s,ite=100,w_new, b_new,lr=0.001):

        self.l_s = l_s
        self.x = x
        self.y = y
        self.m = m
        self.b = b
        self.ite = ite
        self.w_new = w_new
        self.b_new = b_new
        self.lr = lr

    def least_square(self):
        self.l_s = 0
        for i in range(len(self.x)):
            self.l_s += np.square((self.y[i] - self.m * self.x[i] - self.b))
        return self.l_s / len(self.x)

    def update_w(self):
        for i in range(len(self.x)):
            self.w_new += (-1 * (2 * self.x[i] * (self.y[i] - self.m * self.x[i] - self.b)))
        return self.w_new / len(self.x)


    def update_b(self):
        for i in range(len(self.x)):
            self.b_new += (-1*(2 * (self.y[i] - self.m * self.x[i] - self.b)))
        return self.b_new / len(self.x)



    def fit(self):
        for j in range(self.ite):
            self.m -= self.update_w()
            self.b -= self.update_b()
















