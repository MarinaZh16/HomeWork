while 1:
        print('Введите число')
        m=abs(int(input()))
        n=len(str(m))-1
        for x in range(n, -1, -1):
                d=10**x
                b=m//d
                c=b*d
                m=m%d
                print('%s = %s * %s ' %(c, b ,d))
        

        
    
       


    
            
                
                    
            
