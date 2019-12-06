import numpy as np

# def AND(x1,x2):
#     x=np.array([x1,x2])
#     w=np.array([0.5,0.5])
#     b=-0.7
#     tmp = np.sum(x*w)+b
#     if tmp<=0 :
#         return 0
#     else :
#         return 1

# def OR(x1,x2):
#     x=np.array([x1,x2])
#     w=np.array([0.5,0.5])
#     b=-0.2
#     tmp = np.sum(x*w)+b
#     if tmp<=0 :
#         return 0
#     else :
#         return 1

def NAND(x1,x2):                # universal gate
    x=np.array([x1,x2])         # x : input signal
    w=np.array([-0.5,-0.5])     # w : weight
    b=0.7                       # b : bias
    tmp = np.sum(x*w)+b
    if tmp<=0 :
        return 0
    else :
        return 1

def NOT(x1):
    y=NAND(x1,x1)
    return y

def AND(x1,x2):
    s=NAND(x1,x2)
    y=NOT(s)            # y=NAND(s,s)
    return y

def OR(x1,x2):
    s1=NOT(x1)          # s1=NAND(x1,x1)
    s2=NOT(x2)          # s2=NAND(x2,x2) 
    y=NAND(s1,s2)       
    return y

def NOR(x1,x2):
    s=OR(x1,x2)
    y=NOT(s)
    return y

def XOR(x1,x2):
    s1=NAND(x1,x2)
    s2=OR(x1,x2)
    y=AND(s1,s2)
    return y

# nor gate is also universal gate.

# test
for i in range(2) :
    for j in range(2) :
        print("{0} and {1} -> {2}".format(i,j,AND(i,j)))

for i in range(2) :
    for j in range(2) :
        print("{0} or {1} -> {2}".format(i,j,OR(i,j)))
        
for i in range(2) :
    for j in range(2) :
        print("{0} nand {1} -> {2}".format(i,j,NAND(i,j)))

for i in range(2) :
    for j in range(2) :
        print("{0} xor {1} -> {2}".format(i,j,XOR(i,j)))