import sys
s=1
F=open('fizz_buzz.txt', 'w')
F.close 
while s:
    F_B=str()
    file = open('nums1.txt', mode='r', encoding='utf-8-sig')
    print('Введите номер строки')
    q=int(input())
    if q<=20:
        q-=1
        f=file.readlines()[q]
        p=f.split(' ')
        fizz=int(p[0])
        buzz=int(p[1])
        n=int(p[2])
        F_B+=('Числа в строке № %s : %s, %s, %s\n--Результат:'%(q+1, fizz, buzz, n))
        for i in range(1, n):
            if not i%fizz and not i%buzz:
                F_B+='FB '
            elif not i%fizz:
                F_B+='F '
            elif not i%buzz:
                F_B+='B '
            else:
                F_B+=str(i)+' '
        print(F_B)
        F=open('fizz_buzz.txt', 'a')
        F.write(F_B + '\n')
    else:
        F.write('На этом всё!\nДо скорых встреч!')
        print('На этом всё!\nДо скорых встреч!')
        break

    
        

    
F.close()   





