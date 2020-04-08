def len_dif(x, y):
    difference=[]
    for i in range(len(x)):
        dif=abs(len(x[i])-len(y[i]))
        difference.append(dif)
    k=difference.index(max(difference))
    return max(difference), k

              
l_1=['How to pay the witcher?', 'Luke, I am your father!', 'May the force be with you']
l_2=['Minted coin, minted coin', 'Nooooooo!', 'May the force be with you']
res=list(len_dif(l_1, l_2))
print(l_1[res[1]]+'\n'+l_2[res[1]])
print('Length difference between lines = %s' %(res[0]))
