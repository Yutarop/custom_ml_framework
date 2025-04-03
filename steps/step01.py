import numpy as np


class Variable:
    def __init__(self, data):
        self.data = data

# example of how to use variable class
data = np.array(1.0)
x = Variable(data)
# print(x.data)