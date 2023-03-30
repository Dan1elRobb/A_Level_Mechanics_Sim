import easygui
from main import N_L_Two_No_Mass, N_L_Two_No_Force, N_L_Two_No_Acc
msg = 'Select NL2 Question Type'
title = ''
choices = ['No Force', 'No Mass', 'No Acceleration']

mes = 'Input Variables'
sentry = True
while sentry:
    type_question = easygui.choicebox(msg, title, choices)
    if type_question == 'No Force':
        var = ['Mass', 'Acc', 'Direction']
        entry = easygui.multenterbox(mes, title, var)
        answer = N_L_Two_No_Force(float(entry[0]), float(entry[1]), entry[2])
        display = easygui.msgbox(answer)

    if type_question == 'No Mass':
        var = ['Force', 'Acc']
        entry = easygui.multenterbox(mes, title, var)
        answer = N_L_Two_No_Mass(float(entry[0]), float(entry[1]))
        display = easygui.msgbox(answer)

    if type_question == 'No Acceleration':
        var = ['Force', 'Mass', 'Direction']
        entry = easygui.multenterbox(mes, title, var)
        answer = N_L_Two_No_Acc(float(entry[0]), float(entry[1]), entry[2])
        display = easygui.msgbox(answer)

    cont = easygui.ccbox()
    if not cont:
        sentry = False





