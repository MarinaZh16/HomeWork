def floor_func(apartment, n_floors, q_apartments):
    aps_f_d=n_floors*q_apartments           # кол-во квартир в одном подъезде
    if apartment<=aps_f_d:                  # узнаём, в каком подъезде нужная нам
        front_door=1                        # квартира
    elif apartment%aps_f_d ==0:
        front_door=apartment//aps_f_d
    else:
        front_door=apartment//aps_f_d +1
    if front_door==1:
        if apartment%q_apartments==0:       # находим этаж
            floor=apartment//q_apartments
        else:
            floor=apartment//q_apartments+1
    else:
        ap_f_d=apartment-((front_door-1)*aps_f_d)
        if ap_f_d%q_apartments==0:
            floor=ap_f_d//q_apartments
        else:
            floor=ap_f_d//q_apartments+1
    return (print('Front door № %s, floor %s' %(front_door, floor)))






print('Enter the apartment number:')
apartment=int(input())
print('Enter the number of floors in the house:')
n_floors=int(input())
print('How many apartments are there per floor?')
q_apartments=int(input())
res=floor_func(apartment, n_floors, q_apartments)
