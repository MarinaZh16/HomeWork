import sys
import random
from random import randrange
def clean_file(file):
    N=open(file, 'w')
    N.close

def read_file(file):
    N=open(file, mode='r', encoding='utf-8-sig')
    return N
def write_file(file, result):
    N=open(file, 'a')
    N.write(result + '\n')
    N.close
    

def list_generate(length, q, filename):
    file=clean_file(filename)
    n_1=[i for i in range (1, length) if i <11 and not i%2==0]
    n_2=[i for i in range (1, length) if i %2==0]
    n_3=[i for i in range (1, length) if i >11]
    for j in range(q):
        x=randrange(len(n_1))
        y=randrange(len(n_2))
        z= randrange(len(n_3))
        res='%s %s %s' %(n_1[x], n_2[y], n_3[z])
        N=write_file(filename, res)          

#*************************************************************
file=list_generate(40, 21, 'numbers1.txt')
file=read_file('numbers1.txt')
F=clean_file('f_b.txt')
for i in range(20):
        F_B=str()
        f=file.readline()
        p=f.split(' ')
        fizz=int(p[0])
        buzz=int(p[1])
        n=int(p[2])
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
        F=write_file('f_b.txt', F_B)

file.close()
    
