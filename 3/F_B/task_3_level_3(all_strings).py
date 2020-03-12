import sys
file = open('nums1.txt', mode='r', encoding='utf-8-sig')
F=open('f_b.txt', 'w')
F.close 
for i in range(20):
    F_B=str()
    f=file.readline()
    p=f.split(' ')
    fizz=int(p[0])
    buzz=int(p[1])
    n=int(p[2])
    #print(fizz, buzz, n)
    for i in range(1, n+1):
        if not i%fizz and not i%buzz:
            F_B+='FB '
        elif not i%fizz:
            F_B+='F '
        elif not i%buzz:
            F_B+='B '
        else:
            F_B+=str(i)+' '
        
    print(F_B)
    F=open('f_b.txt', 'a')
    F.write(F_B + '\n')
    

file.close()
F.close()

        
        
        
    


