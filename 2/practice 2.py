
while 1:
    print('Enter the number')
    a=int(input())
    if not(a%2)==0 and (a%3)==0 and (a%5)==0 and not(a%9)==0:
        print ('YES')
    else:
        print ('NO')
    
