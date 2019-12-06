import numpy as np
import matplotlib.pylab as plt

#before using sigmoid function.
def step_function(x) :
    y= x>0
    return y.astype(np.int)
    # return np.astype(x>0,dtype=np.int)

x=np.arange(-5.0,5.0,0.1)
y=step_function(x)
plt.plot(x,y)

#before using relu function.
def sigmoid(x) :
    return 1/(1+np.exp(-x))         # 배열을 넣어도 배열로 리턴. 이게 편한듯.  numpy 꼭 기억.

z=sigmoid(x)
plt.plot(x,z)
plt.show()


def relu(x) :
    return np.maximum(0,x)

