for i in range(1,101):
    rightint = int(str(i)[-1])
    if i == 1:
        v_end = ' процент'
    elif i < 5:
        v_end = ' процента'

    elif rightint == 1 and i>20:
        v_end = ' процент'
    elif rightint < 5  and i>20 and rightint != 0:
        v_end = ' процента'
    else:
       v_end = ' процентов'

    print(i, v_end)


