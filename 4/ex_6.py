from random import randint
s=[(randint(1, 20)) for i in range(20)]
#print(s)
while 1:
    print('Enter the number:')
    n=int(input())                      # Вариант 1
    if any(n==x for x in s):
        print('''Yessss, it's there!''')
        print('*'*19)
        break
    else:
        print('''It's not there :( Try again''')
        
        


#***************************************************
while 1:                                # Вариант 2
    print('Enter the number:')          # можно посчитать сколько раз число
    n=int(input())                      # встречается в списке
    if s.count(n)>=1:            
        print('''Yessss, it's there! %s times!''' %(s.count(n)))
        break
    else:
        print('''It's not there :( Try again!''')
