"""the module into which classes Employee, Programmer, Recruiter, Candidate
and Vacancy are imported and instances of these classes are created"""
from progr_recr import Programmer, Recruiter
from candidate import Candidate
from vacancy import Vacancy

if __name__ == '__main__':
    programmer_1 = Programmer('Marina', 'Zhidkova', 'mzh@gmail.com', '066xxxxxxx',
                              22, ['python', 'C++', 'Ruby', 'C'], 3)
    programmer_2 = Programmer('Vlad', 'Zhidkov', 'vzh@gmail.com', '066xxxxxxx',
                              23, ['python', 'C++', 'Java'], 2)
    rectuiter_1 = Recruiter('Yasha', 'Kulbaka', 'yak@gmail.com',
                            '099xxxxxxx', 19, 2)
    candidate_1 = Candidate('Alesya Lunyova', 'alun@gmail.com',
                            ['Python', 'PHP'], 'Python', 'junior')
    candidate_2 = Candidate('Igor Samusenko', 'isam@gmail.com',
                            ['Python', 'PHP', 'Java'], 'PHP', 'senior')
    candidate_3 = Candidate('Julia Sokolyk', 'jsok@gmail.com',
                            ['C++', 'PHP', 'Java'], 'C++', 'middle')
    vacancy_1 = Vacancy('Full-Stack Developer', 'PHP', 'middle')
    vacancy_2 = Vacancy('C++ Developer', 'C++', 'middle')
