import math
def calc_v_over_time(angle, mew, end_time):

    t = 0
    time_list = []
    vel_list = []
    acc = 9.8 * math.sin(math.radians(angle)) - 9.8 * math.cos(math.radians(angle)) * mew
    while t < end_time:
        v = acc * t
        vel_list.append(v)
        time_list.append(t)
        t += 0.01
    return vel_list, time_list

v = calc_v_over_time(30,0.3,15)[0]
t = calc_v_over_time(30,0.3,15)[1]

print(t[500],v[500])

a = [i for i in range(100)]
print(a)