"""module that holds classes Programmer and Rectuiter"""
from employee import Employee

class Programmer(Employee):
    """class that inherits from class Empliyee"""
    def __init__(self, name, surname, email, phone_number, salary, tech_stack,
                 closed_this_monht):
        super().__init__(name, surname, email, phone_number, salary)
        self.tech_stack = tech_stack
        self.closed_this_monht = closed_this_monht

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
        """overriding the work method"""
        emp_work = super().work()[:-1]
        return emp_work + ' and start coding'

    def super_p(self, other):
        """a method by which you can create a super-programmer
        from two ordinary, summing up their properties"""
        tech_stack = self.tech_stack+other.tech_stack
        closed_this_monht = self.closed_this_monht + other.closed_this_monht
        return 'Superskills: %s ; number of closed tasks : %s'\
    %(list(set(tech_stack)), closed_this_monht)


class Recruiter(Employee):
    """class that inherits from class Empliyee"""
    def __init__(self, name, surname, email, phone_number, salary,
                 hired_this_monht):
        super().__init__(name, surname, email, phone_number, salary)
        self.hired_this_monht = hired_this_monht

    def work(self):
        """overriding the work method"""
        emp_work = super().work()[:-1]
        return emp_work + ' and start hiring'
