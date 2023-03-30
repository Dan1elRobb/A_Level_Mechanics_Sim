import pymunk


def N_L_Two_No_Force(mass, acceleration, direction):
    resultant_force = mass * acceleration
    return f'{resultant_force}N in the {direction} direction'


def N_L_Two_No_Acc( resultant_force, mass, direction):
    acc = resultant_force / mass
    return f'{acc}m/s^2 in the {direction} direction'


def N_L_Two_No_Mass(resultant_force,acceleration,):
    mass = resultant_force / acceleration
    return f'{mass}kg'


a = N_L_Two_No_Force(4, 5, 'right')
b = N_L_Two_No_Acc(4, 20, 'right')
c = N_L_Two_No_Mass(5, 20)
print(a)
print(b)
print(c)
