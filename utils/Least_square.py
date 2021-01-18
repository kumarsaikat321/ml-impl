import numpy as np


class least_sq:
    def __init__(self, x, y, n, w=0.0, b=0.0, weight_mat=0):

        self.weight_mat = weight_mat
        self.x = x  # taking input of x
        self.y = y
        self.n = n
        self.w = w
        self.b = b

    def fit(self):

        global output
        b = 0.001
        for i in range(1, self.n):
            self.w = np.array(i)
            self.x = np.array(i)
            self.weight_mat = self.x * self.w
            self.weight_mat = sum(self.weight_mat)

            for j in range(1, self.n):
                self.y[j] = b + self.weight_mat
                output = self.y[j]

            return output
