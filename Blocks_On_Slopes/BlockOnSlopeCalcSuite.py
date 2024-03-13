import math
G = 9.8


def calc_a(m, angle, mew):
    r = m * G * math.cos(math.radians(angle))
    f = mew * r
    a = (m * G * math.sin(math.radians(angle)) - f) / m
    return a


def calc_m(f, angle, mew):
    m = f / (mew * G * math.cos(math.radians(angle)))
    return m


def calc_f_m(mew, m, angle):
    f = mew * m * G * math.cos(math.radians(angle))
    return f


def calc_angle(f, mew, m):
    angle = math.acos(f / (mew * m * G))
    return math.degrees(angle)


def calc_m_with_acc(angle, a, f):
    m = f / ((G * math.sin(math.radians(angle))) - a)
    return m


def calc_v_over_time(angle, mew, end_time):
    t = 0
    time_list = []
    vel_list = []
    while t < end_time:
        v = 9.8 * t * (math.sin(angle) - math.cos(angle) * mew)
        vel_list.append(v)
        time_list.append(t)
        t += 0.01
    return vel_list, time_list


print(calc_v_over_time(60, 0.5, 10))

