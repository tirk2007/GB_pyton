duratoin = int(input('Введите число секунд: '))

if duratoin < 60:
    print(duratoin,' сек')
elif duratoin < 3600:
    print(duratoin // 60, ' мин', duratoin % 60, ' сек' )
elif duratoin < 86400:
    r_hour = duratoin // 3600
    r_min = (duratoin - r_hour * 3600) // 60
    r_sec = duratoin - (r_hour * 3600 + r_min * 60)
    print(r_hour,' час',r_min,' мин',r_sec,' сек')
else:
    r_day  = duratoin // 86400
    duratoin = duratoin - r_day * 86400
    r_hour = duratoin // 3600
    r_min = (duratoin - r_hour * 3600) // 60
    r_sec = duratoin - (r_hour * 3600 + r_min * 60)
    print(r_day, ' дн', r_hour, ' час', r_min, ' мин', r_sec, ' сек')




