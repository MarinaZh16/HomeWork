def sqw_ar(num):
    s=[i for i in range (1, num+1) if num%i==0]
    if len(s)==2 or num==1:
        return num**2
    else:
        return num
        
       
l=list(range(1, 35))
square_list=list(map(sqw_ar, l))
