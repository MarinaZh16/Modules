"""module that holds class Employee"""
from datetime import datetime
class Employee(object):
    """class where employee information is stored"""
    def __init__(self, name, surname, email, phone_number, salary):
        """Constructor"""
        self.name = name
        self.surname = surname
        self.email = email
        self.phone_number = phone_number
        self.salary = salary
        try:
            self.validate_email()
        except FileNotFoundError:
            print('email.txt file was not found.  '
                  'No validation provided')
        self.save_email()
        
    """here is a miscalculation of the number of working days
    from the beginning of the current month to the present"""
    from datetime import date, timedelta
    now = date.today()
    month_start = date(now.year, now.month, 1)
    weekend = [5, 6]
    diff = (now - month_start).days + 1
    day_count = 0
    for day in range(diff):
        if(month_start + timedelta(day)).weekday() not in weekend:
            day_count += 1
    

    def save_email(self):
        with open('email.txt', 'a') as f:
            f.write(self.email)
            f.write('\n')

    def validate_email(self):
        with open('email.txt', 'r') as f:
            for line in f:
                if self.email in line:
                    #print(self.email, 'such email allready exsists')
                    raise ValueError('such email allready exsists')            
                
    def work(self):
        """returns a string 'I come to the office.'"""
        return 'I come to the office.'

    def check_salary(self, days=day_count):
        """salary calculation method depending on the number
    of working days or current salary from the beginning
    of the month"""
        return self.salary * days

    def __lt__(self, other):
        print('LT')
        return self.salary < other.salary 

    def __gt__(self, other):
        print('GT')
        return self.salary > other.salary
        
    def __eq__(self, other):
        print('EQ')
        return self.salary == other.salary

    def __le__(self, other):
        print('LE')
        return self.salary <= other.salary

    def __ge__(self, other):
        print('GE')
        return self.salary >= other.salary

    def __ne__(self, other):
        print('NE')
        return self.salary != other.salary

    def __str__(self):
        return '%s: %s %s' %(self.__class__.__name__, self.name, self.surname)
