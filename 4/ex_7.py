n=1
s=[]
while n<=1000:
    print('Enter the number:')
    n=int(input())
    s.append(n)
s.pop()
S_average=round(sum(s)/len(s))
print(s)
print('''Сумма всех введенных чисел = %s;
Среднее число = %s;
Максимальное число = %s;
Минимальное число = %s''' %(sum(s), S_average, max(s), min(s)))    
