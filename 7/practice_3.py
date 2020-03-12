import sys
file=open('strings.txt', mode='r', encoding='utf-8-sig')
for i in range(14):
    r=file.readline()
    p=r.split(';')
    n_list=(p[0].split(' '))
    r_list=p[1].split(' ')
    nums=[]
    res=[]
    for i in range(len(n_list)):
        nums.append(int(n_list[i]))
    for j in range(len(r_list)):
        res.append(int(r_list[j]))
    d_m=list(divmod(sum(nums), len(nums)))
    if d_m==res:
        print(r, 'True')
    else:
        print(r, 'False')
    
