import numpy as np
import matplotlib.pyplot  as plt
import math

a=[]
b=[]

y=0
x=int(input("X egal cu "))
pnct=int(input("Numarul de puncte este egal cu "))


fig, ax = plt.subplots()

for i in range (pnct):
    if x > 10:
        y=x**2-6*x-1
        x = x + 1
    else:
        y = y*2 + 1
        x = x + 1
    a.append(x)
    b.append(y)
    ax.plot(a, b)
    plt.pause(0.001)

plt.show()
