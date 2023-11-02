import math
import matplotlib.pyplot as plt

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

print(calc_v_over_time(30,0.5,10))

fig = plt.figure()
ax = plt.axes()
ax.plot(calc_v_over_time(30,0.5,10)[0],calc_v_over_time(30,0.5,10)[1])