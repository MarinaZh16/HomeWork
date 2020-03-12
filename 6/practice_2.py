students={'Bruse Wayne', 'Piter Parker', 'Clark Kent', 'Tony Stark', 'Eddie Brock'}
courses=['Python', 'FullStack', 'FrontEnd', 'Java']
groups={'Bruse Wayne': ('Python', 'FullStack'), 'Piter Parker': ('FrontEnd', 'Java'), 'Clark Kent': ('Python', 'FrontEnd'),'Tony Stark': ('Java', 'Python'), 'Eddie Brock': ('Python', 'Java')}
print('All students who study Python and Java are:')
for i in students:
    if courses[0] or courses[3] in groups[i]:
        print(i)
print('*'*43)
for i in groups:
    if len(groups[i])>=2:
            print('%s is studying %s courses' %(i,len(groups[i])))
print('*'*43)
print('''All students who don't study FrontEnd are:''')
for i in groups:
    if not courses[2]in groups[i]:
        print(i)
