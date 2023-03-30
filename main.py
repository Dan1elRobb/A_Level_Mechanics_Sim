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


