money=[10, 20, 50, 100, 500, 1000]
s=1
while s <= 20000 and s%10!=0:
    print('Введите сумму, кратую 10')
    s=abs(int(input()))
    if s > 20000:
        print('''Банкомат не выдёт больше 20000 за одну транзакцию.\nВведите другую сумму, кратную 10''')
        s=abs(int(input()))
    p=len(money)-1
    q=s
for i in range(p, -1, -1):
    m=q//money[i]
    q=q%money[i]
    if m > 0:
        if m == 1:
            print('%s купюра номиналом %s' %(m, money[i]))
        elif 2 <= m <5:
            print('%s купюры номиналом %s' %(m, money[i]))
        elif 5 <= m < 21:
            print('%s купюр номиналом %s' %(m, money[i]))
        money.pop()
            
       


