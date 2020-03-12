from random import randint
S=[(randint(50, 500)) for i in range(10)]
S.sort()
#print(S)
t=[(randint(5, 60)) for i in range(10)]
t.sort()
#print(t)
V=[round(S[x]/t[x]) for x in range(10)]  
#print(V)
V_average=round(sum(V)/10)
print('Средняя скорость = %s км/ч' %(V_average))
for i in range(10):
    c=V.count(V[i]<V_average)  
    if V[i]>V_average:
        print(' Скорость %s км/ч превышает среднюю' %(V[i]))
    
