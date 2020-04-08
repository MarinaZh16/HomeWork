n=-2
while (n%2)==0 :
    print('Enter the number from 1 to 101 inclusive')
    n=abs(int(input()))
    if n>20:
        p=n//2+1
    else:
        p=10                        # задам кол-во пробелов для выравнивания
    for i in range(1, n+1//2, 2):    
        q=i                         # определяем кол-во звёздочек в ряду
        print(' '*p, '*'*q)
        p-=1                        # корректируем кол-во пробелов
    for i in range(n+1//2, 0, -2):  # то же самое в обратном порядке 
        q=i
        print(' '*p, '*'*q)
        p+=1
       
        
