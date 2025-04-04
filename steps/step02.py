import numpy as np
from step01 import Variable

class Function:
    def __call__(self, input):
        x = input.data
        y = self.forward(x)
        output = Variable(y)
        self.input = input # store a value that is passed through
        return output
    
    # set function when using this object
    def forward(self, x):
        raise NotImplementedError()
    
    def backward(self, gy):
        raise NotImplementedError()

# example of how to use function class
class Square(Function):
    def forward(self, x):
        y = x ** 2
        return y
    
    def backward(self, gy):
        x = self.input.data
        gx = 2 * x * gy
        return gx
    
# x = Variable(np.array(10))
# f = Square()
# y = f(x)
# print(type(y))
# print(y.data)
