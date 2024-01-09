import math


def calc_variables_over_time(angle, end_time, initial_vel, initial_height):
    t = 0
    time_list = []
    y_dis_list = []
    x_dis_list = []
    y_vel_list = []
    while t < end_time:
        y_s = initial_vel * math.sin(math.radians(angle)) * t - 4.9 * t ** 2 + initial_height
        x_s = initial_vel * math.cos(math.radians(angle)) * t
        y_vel = initial_vel * math.sin(math.radians(angle)) - (9.8 * t)
        y_dis_list.append(abs(y_s))
        x_dis_list.append(x_s)
        y_vel_list.append(y_vel)
        time_list.append(t)
        t += 0.01
    return time_list, y_dis_list, x_dis_list, y_vel_list


print(calc_variables_over_time(30, 15, 15, 0)[0])
print(calc_variables_over_time(30, 15, 15, 0)[1])

