import math
import matplotlib.pyplot as plt
import numpy as np


class h_function:
    @staticmethod
    def h(t):
        lamb = 5 * math.sin(2 * math.pi * t)
        h_v = 3 * math.pi * math.exp(-lamb)
        return h_v

def main():
    x = h_function()
    time = 0
    ti = []
    h_v_1 = []
    while time<2.5:
        time=time+0.01
        h_v = x.h(time)        
        ti.append(time)
        h_v_1.append(h_v)

    plt.plot(ti,h_v_1)
    plt.xlabel('time (s)')
    plt.ylabel('h(t)')
    plt.show()

if __name__ == '__main__':
    main()
