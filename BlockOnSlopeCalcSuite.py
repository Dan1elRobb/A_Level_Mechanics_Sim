import math
import easygui

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
        v = 9.8 * t*(math.sin(angle) - math.cos(angle) * mew)
        vel_list.append(v)
        time_list.append(t)
        t += 0.01
    return vel_list, time_list

print(calc_v_over_time(60, 0.5, 10))
'''m = int(input('Mass: '))
angle = int(input('Angle: '))
f = int(input('Friction: '))
mew = float(input('Mew: '))
a = int(input('Acceleration: ')

message = 'Enter the question variables'
box_title = 'Blocks on slopes'
var_names = ['Mass', 'Angle', 'Friction', 'Coefficient of Friction', 'Acceleration']
var_values = []
var_values = easygui.multenterbox(message, box_title, var_names)

m = int(var_values[0])
angle = int(var_values[1])
f = int(var_values[2])
mew = int(var_values[3])
a = int(var_values[4])

if m == -1 and a != -1 and angle != -1 and f != -1:
    m = calc_m_with_acc(angle, a, f)
    print(m)
if m == -1 and mew != -1 and angle != -1 and f != -1:
    m = calc_m(f, angle, mew)
    print(m)
if a == -1 and angle != -1 and mew != -1 and m != -1:
    a = calc_a(m, angle, mew)
    print(a)
if f == -1 and mew != -1 and m != -1 and angle != -1:
    f = calc_f_m(mew, m, angle)
    print(f)
if angle == -1 and f != -1 and mew != -1 and m != -1:
    angle = calc_angle(f, mew, m)
    print(angle)
    '''
