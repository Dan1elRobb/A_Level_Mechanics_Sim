import math
import easygui
G = 9.8


def calc_a(m, angle, mew):
    r = m * G * math.cos(angle)
    f = mew * r
    a = (m * G * math.sin(angle) - f) / m
    return a


def calc_m(f, angle, mew):
    m = f / (mew * G * math.cos(angle))
    return m


def calc_f_m(mew, m, angle):
    f = mew * m * G * math.cos(angle)
    return f

def calc_angle(f, mew, m):
    angle = math.acos(f/(mew*m*G))
    return angle


m = int(input('Mass: '))
angle = int(input('Angle: '))
