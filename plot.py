from math import exp

import matplotlib.pyplot as plt
import numpy as np

def calc_limit_1(temp) -> int:
    """ Calculate limit for risk level 1 """
    if 0 <= temp <= 50:
        limit = 20 * exp( -temp * 0.15 ) + 73
        return max(min(100,limit),72)
    else:
        return 100

def calc_limit_2(temp) -> int:
    """ Calculate limit for risk level 2 """
    if 0 <= temp <= 50:
        limit = 17 * exp( -temp * 0.11 ) + 80
        return max(min(100,limit),79)
    else:
        return 100
    
def calc_limit_3(temp) -> int:
    """ Calculate limit for risk level 3 """
    if 0 <= temp <= 50:
        limit = 15 * exp( -temp * 0.10 ) + 85
        return max(min(100,limit),84)
    else:
        return 100

temp = np.arange(-10., 60., 0.5)
y1 = [calc_limit_1(x) for x in temp]
plt.plot(temp, y1)
y2 = [calc_limit_2(x) for x in temp]
plt.plot(temp, y2)
y3 = [calc_limit_3(x) for x in temp]
plt.plot(temp, y3)
plt.xlabel('Temperature (°C)')
plt.ylabel('RH (%)')
plt.grid(True)
plt.axis([-10,60,70,100])
plt.show()