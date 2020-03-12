numbers=[]                                          #вариант 1
for x in range(1, 20):
    if not x%2==0:
        numbers.append(x*x*x)
print(numbers)        
    
print('----------------------------------------------------')

nums=[x*x*x for x in range(1, 20) if not x%2==0]    #вариант 2
print(nums)


          
