while 1:
    print('Enter the number:')
    a=int(input())
    s=[i for i in range (1, a+1) if a%i==0]        
    if len(s)==2 or a==1:
        print('Number %s is simple' %(a))
    else:
        print('Number %s is NOT simple' %(a))
        
            
