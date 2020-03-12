import sys
while 1:
    file = open('nums1.txt', mode='r', encoding='utf-8-sig')
    print('Введите номер строки')
    q=int(input())
    if q<=20:
        q-=1                    # чтобы вывод начинался с нулевой строки, которую
        f=file.readlines()[q]   # пользователь считает первой
        p=f.split(' ')
        fizz=int(p[0])          # присваиваем значения, взятые из строки, 
        buzz=int(p[1])          # переменным
        n=int(p[2])
        print('Числа в строке № %s : %s %s %s\n--Результат:'%(q+1, fizz, buzz, n))
        for i in range(1, n):
            if not i%fizz and not i%buzz:
                print('FB', end = ' ')
            elif not i%fizz:
                print('F', end = ' ')
            elif not i%buzz:
                print('B', end = ' ')
            else:
                print(i, end = ' ')
        print('\n')
    else:
        print('На этом всё!')
        break
        
print('До скорых встреч!')

file.close()

