def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k, v

students=('Bruse Wayne', 'Piter Parker', 'Clark Kent', 'Tony Stark', 'Eddie Brock')
marks=((100, 80, 95, 90), (70, 40, 80,85), (95, 75, 100,80), (65, 90, 70, 70), (75, 85, 95, 100))
stm=dict(zip(students, marks))
#print(stm)
stm_m=dict()
for i in stm:
    m=round(sum(stm[i])/len(stm[i]))
    stm_m[i]=m
#print(stm_m)
most_successful= get_key(stm_m, max(stm_m.values()))
less_successful=get_key(stm_m, min(stm_m.values()))
print('the most sucessful student is %s, his average mark is %s'%(most_successful[0], most_successful[1]))
print('the less sucessful student is %s, his average mark is %s'%(less_successful[0], less_successful[1]))
