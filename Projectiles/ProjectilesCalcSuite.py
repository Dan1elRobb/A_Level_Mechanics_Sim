import math


def calc_y_v_over_time(angle, end_time, initial_vel):
    t = 0
    time_list = []
    vel_list = []
    while t < end_time:
        v = initial_vel * math.sin(angle) - 9.8 * t
        vel_list.append(v)
        time_list.append(t)
        t += 0.01
    return vel_list, time_list


def calc_x_s_over_time(angle, end_time, initial_vel):
    t = 0
    time_list = []
    dis_list = []
    while t < end_time:
        s = initial_vel * math.cos(angle) * t
        dis_list.append(s)
        time_list.append(t)
        t += 0.01
    return dis_list, time_list


def calc_y_s_over_time(angle, end_time, initial_vel, initial_height):
    t = 0
    time_list = []
    dis_list = []
    while t < end_time:
        s = initial_vel * math.sin(angle) * t - 4.9 * t ** 2 + initial_height
        dis_list.append(s)
        time_list.append(t)
        t += 0.01
    return dis_list, time_list


def calc_variables_over_time(angle, end_time, initial_vel, initial_height):
    t = 0
    time_list = []
    y_dis_list = []
    x_dis_list = []
    y_vel_list = []
    while t < end_time:
        y_s = initial_vel * math.sin(angle) * t - 4.9 * t ** 2 + initial_height
        x_s = initial_vel * math.cos(angle) * t
        y_vel = initial_vel * math.sin(angle) - 9.8 * t
        y_dis_list.append(y_s)
        x_dis_list.append(x_s)
        y_vel_list.append(y_vel)
        time_list.append(t)
        t += 0.01
    return time_list, y_dis_list, x_dis_list, y_vel_list
