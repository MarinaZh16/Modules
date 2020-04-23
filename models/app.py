"""the module into which classes Employee, Programmer, Recruiter, Candidate
and Vacancy are imported and instances of these classes are created"""

from workers.progr_recr import Programmer, Recruiter
from workers.employee import Employee
from workers.candidate import Candidate
from workers.vacancy import Vacancy

def main():
    p_1 = Programmer('Marina', 'Zhidkova', 'mzh@gmail.com', '066xxxxxxx',
                              22, ['python', 'C++', 'Ruby', 'C'], 3)
    p_2 = Programmer('Vlad', 'Zhidkov', 'vzh@gmail.com', '066xxxxxxx',
                              23, ['python', 'C++', 'Java'], 2)
    r_1 = Recruiter('Yasha', 'Kulbaka', 'yak@gmail.com',
                            '099xxxxxxx', 19, 2)
    c_1 = Candidate('Alesya Lunyova', 'alun@gmail.com',
                            ['Python', 'PHP'], 'Python', 'junior')
    c_2 = Candidate('Igor Samusenko', 'isam@gmail.com',
                            ['Python', 'PHP', 'Java'], 'PHP', 'senior')
    c_3 = Candidate('Julia Sokolyk', 'jsok@gmail.com',
                            ['C++', 'PHP', 'Java'], 'C++', 'middle')
    v_1 = Vacancy('Full-Stack Developer', 'PHP', 'middle')
    v_2 = Vacancy('C++ Developer', 'C++', 'middle')
    print(str(p_1))
    print(r_1.check_salary())
    print(p_1 > p_2)
    print(p_1.info)

    
if __name__ == '__main__':
    main()
