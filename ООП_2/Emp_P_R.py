from datetime import date, timedelta
now=date.today()
month_start=date(now.year, now.month, 1)
weekend=[5, 6]
diff=(now - month_start).days+1
day_count=0
for day in range(diff):
    if(month_start + timedelta(day)).weekday() not in weekend:
        day_count+=1


class Employee:
    def __init__(self, name, surname, email, phone_number, salary):
        self.name=name
        self.surname=surname
        self.email=email
        self.phone_number=phone_number
        self.salary=salary

    def work(self):
        return 'I come to the office.'
        
    def check_salary(self, days=day_count):
        return '%s $' %(self.salary*days)

    def __lt__(self, other):
        return 'LT: %s' %(self.salary < other.salary) 

    def __gt__(self, other):
        return 'GT: %s' %(self.salary > other.salary)
        
    def __eq__(self, other):
        return 'EQ: %s' %(self.salary == other.salary)

    def __le__(self, other):
        return 'LE: %s' %(self.salary <= other.salary)

    def __ge__(self, other):
        return 'GE: %s' %(self.salary >= other.salary)

    def __ne__(self, other):
        return 'NE: %s' %(self.salary != other.salary)
    

class Recruiter(Employee):
    def __init__(self, name, surname, email, phone_number, salary, hired_this_monht):
        super().__init__(name, surname, email, phone_number, salary)
        self.hired_this_monht=hired_this_monht

    def full_salary(self):
        month_start=date(now.year, self.hired_this_monht, 1)
        diff=(now - month_start).days+1
        day_count=0
        for day in range(diff):
            if(month_start + timedelta(day)).weekday() not in weekend:
                day_count+=1        
        return 'Full salary = %s $' %(self.salary*day_count)
        
    def work(self):
        emp_work=super().work()[:-1]
        return emp_work+' and start hiring'

    def __str__(self):
        return 'Recruiter: %s %s' %(self.name, self.surname)


class Programmer(Employee):
    def __init__(self, name, surname, email, phone_number, salary, tech_stack, closed_this_monht):
        super().__init__(name, surname, email, phone_number, salary)
        self.tech_stack=tech_stack
        self.closed_this_monht=closed_this_monht
        
    def __lt__(self, other):
        return 'Stack LT: %s' %(len(self.tech_stack) < len(other.tech_stack))  

    def __gt__(self, other):
        return 'Stack GT: %s' %(len(self.tech_stack) > len(other.tech_stack)) 
        
    def __eq__(self, other):
        return 'Stack EQ:%s' %(len(self.tech_stack) == len(other.tech_stack)) 

    def __le__(self, other):
        return 'Stack LE: %s' %(len(self.tech_stack) <= len(other.tech_stack)) 

    def __ge__(self, other):
        return 'Stack GE:%s' %(len(self.tech_stack) >= len(other.tech_stack)) 
    
    def __ne__(self, other):
        return 'Stack NE: %s' %(len(self.tech_stack) != len(other.tech_stack)) 

    def work(self):
        emp_work=super().work()[:-1]
        return emp_work+' and start coding'
    
    def __str__(self):
        return 'Programmer: %s %s' %(self.name, self.surname)

    def SuperP(self, other):
        tech_stack=self.tech_stack+other.tech_stack
        closed_this_monht=self.closed_this_monht+other.closed_this_monht
        return 'Superskills: %s ; number of closed tasks : %s' %(list(set(tech_stack)), closed_this_monht)

p_1=Programmer('Марина', 'Жидкова', 'mzh@gmail.com', '066xxxxxxx', 22, ['python', 'C++', 'Ruby', 'C'], 3)
r_1=Recruiter('Женя', 'Татарчук', 'zht@gmail.com', '099xxxxxxx', 20, 1)
p_2=Programmer('Влад', 'Жидков', 'vzh@gmail.com', '066xxxxxxx', 23, ['python', 'C++', 'Java'], 2)
r_2=Recruiter('Яша', 'Кульбака', 'yak@gmail.com', '099xxxxxxx', 19, 2)
print(p_1.work())
print(r_1.work())
print(str(p_1))
print(str(r_1))
print(p_1 < p_2)
print(str(p_2), p_2.check_salary())
print(str(r_2), r_2.check_salary(18))
print(str(r_2), r_2.full_salary())
print(r_1<r_2)
print(p_1.SuperP(p_2))
