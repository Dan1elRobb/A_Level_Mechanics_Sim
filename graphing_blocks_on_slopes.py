import math
import matplotlib.pyplot as plt
import numpy as np
def calc_v_over_time(angle,mew,end_time):
    t = 0
    time_list = []
    vel_list = []
    while t < end_time:
        for i in range((end_time*100)+1):
            v = 9.8*t*(math.sin(math.radians(angle)) - math.cos(math.radians(angle))*mew)
            vel_list.append(v)
            time_list.append(t)
            t += 0.01
    return time_list,vel_list

print(max(calc_v_over_time(60,0.5,10)[1]))

fig = plt.figure(figsize=(20,30))
ax = plt.axes()
ax.plot(calc_v_over_time(60,0.5,10)[0],calc_v_over_time(60,0.5,10)[1])
plt.xticks(np.arange(0,max(calc_v_over_time(60,0.5,10)[0])+0.5,0.5))
plt.yticks(np.arange(0,max(calc_v_over_time(60,0.5,10)[1])+0.5,0.5))
plt.xlim(0,10)
plt.ylim(0,max(calc_v_over_time(60,0.5,10)[1]))
plt.show()