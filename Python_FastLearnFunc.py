
'''
import matplotlib.pyplot as plt
import numpy as np


def drawHeartShape():
    t = np.array(0, 2*np.pi, 0.1)
    x = 16*np.sin(t)**3
    y = 13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)
    plt.plot(x, y, 'r')
    plt.show()


'''



import datetime

def countdown(now, strDate):
    countdown = datetime.datetime.strptime(strDate, "%Y-%m-%d %H:%M:%S")
    delta = countdown - now
    day = delta.days
    return day

now = datetime.datetime.now()
print(now.year,now.month,now.day)
print(countdown(now, "2025-01-07 00:00:00"))










