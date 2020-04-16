class Employee:
    def __init__(self, name, surname, email, phone_number, salary):
        self.name = name
        self.surname = surname
        self.email = email
        self.phone_number = phone_number
        self.salary = salary
    from datetime import date, timedelta
    now = date.today()
    month_start = date(now.year, now.month, 1)
    weekend = [5, 6]
    diff = (now - month_start).days + 1
    day_count = 0
    for day in range(diff):
        if(month_start + timedelta(day)).weekday() not in weekend:
            day_count += 1

    def work(self):
        return 'I come to the office.'
        
    def check_salary(self, days=day_count):
        return '%s $' %(self.salary * days)

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

    def __str__(self):
        return '%s: %s %s' %(self.__class__.__name__, self.name, self.surname)
    

class Recruiter(Employee):
    def __init__(self, name, surname, email, phone_number, salary,
                 hired_this_month):
        super().__init__(name, surname, email, phone_number, salary)
        self.hired_this_month = hired_this_month

    def work(self):
        emp_work = super().work()[:-1]
        return emp_work + ' and start hiring'


class Programmer(Employee):
    def __init__(self, name, surname, email, phone_number, salary, tech_stack,
                 closed_this_month):
        super().__init__(name, surname, email, phone_number, salary)
        self.tech_stack = tech_stack
        self.closed_this_month = closed_this_month

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
        emp_work = super().work()[:-1]
        return emp_work + ' and start coding'
    
    def super_p(self, other):
        tech_stack = self.tech_stack + other.tech_stack
        closed_this_month = self.closed_this_month + other.closed_this_month
        return 'Superskills: %s ; number of closed tasks : %s'\
               %(list(set(tech_stack)), closed_this_month)


P1 = Programmer('Marina', 'Zhidkova', 'mzh@gmail.com', '066xxxxxxx', 22,
                ['python', 'C++', 'Ruby', 'C'], 3)
P2 = Programmer('Vlad', 'Zhidkov', 'vzh@gmail.com', '066xxxxxxx', 23,
                ['python', 'C++', 'Java'], 2)
R1 = Recruiter('Zhenya', 'Tatarchuk', 'zht@gmail.com', '099xxxxxxx', 22, 1)
R2 = Recruiter('Yasha', 'Kulbaka', 'yak@gmail.com', '099xxxxxxx', 19, 2)
print(P1.work())
print(R1.work())
print(str(P1))
print(str(R1))
print(P1 < P2)
print(str(P2), P2.check_salary())
print(str(P2), P2.check_salary(18))
print(R1 < R2)
print(R1 == P1)
print(P1.super_p(P2))

