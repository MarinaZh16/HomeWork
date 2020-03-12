from collections import Counter
from random import choice, randint
import sys
person=[]
superhero=[]
more_people=[]
name=['Bruse', 'Piter', 'Clark', 'Tony', 'Eddie']
#print(name)
surname=['Wayne', 'Parker', 'Kent', 'Stark', 'Brock']
#print(surname)

for i in range(5):              #создаём список супергероев
    s = name[i]+' '+ surname[i] 
    superhero.append(s)


for i in range(5):
    for j in range(5):                  #создаём список всех возможных 
        p=s = name[i]+' '+ surname[j]   #комбинаций имени и фамилии
        more_people.append(p)
#print(more_people)
        

for i in range(25):
    man = choice(name)+' '+ choice(surname) #создаём список случайных
    person.append(man)                      #людей


print('------------------------') 


print('SUPERHEROES:')    
for i in range(5):                          #ищем супергероев в списке
    c=person.count(superhero[i])            #случайных людей
    if c>0:
        if c==1:
            print(' I met %s  once' %(superhero[i]))
        elif c ==2:
             print(' I met %s  twice' %(superhero[i]))
        else:
            print(' I met %s  %s times' %(superhero[i], c ))

print('------------------------') 

for i in range(25):
    c=person.count(more_people[i])                  #разных людей в списке
    if c>0:                                         #случайных людей
        if c==1:
            print(' I met %s  once' %(more_people[i]))
        elif c ==2:
             print(' I met %s  twice' %(more_people[i]))
        else:
            print(' I met %s  %s times' %(more_people[i], c ))

print('------------------------')  

    


        
    
