from progr_recr import Programmer, Recruiter
from candidate import Candidate
from vacancy import Vacancy

if __name__ == '__main__':
    P1 = Programmer('Marina', 'Zhidkova', 'mzh@gmail.com', '066xxxxxxx', 22,
                    ['python', 'C++', 'Ruby', 'C'], 3)
    P2 = Programmer('Vlad', 'Zhidkov', 'vzh@gmail.com', '066xxxxxxx', 23,
                    ['python', 'C++', 'Java'], 2)
    R1 = Recruiter('Zhenya', 'Tatarchuk', 'zht@gmail.com', '099xxxxxxx', 22, 1)
    R2 = Recruiter('Yasha', 'Kulbaka', 'yak@gmail.com', '099xxxxxxx', 19, 2)
    C1 = Candidate('Alesya Lunyova', 'alun@gmail.com', ['Python', 'PHP'],
                   'Python', 'junior')
    C2 = Candidate('Igor Samusenko', 'isam@gmail.com', ['Python', 'PHP', 'Java'],
                   'PHP', 'senior')
    C3 = Candidate('Julia Sokolyk', 'jsok@gmail.com', ['C++', 'PHP', 'Java'],
                   'C++', 'middle')
    V1 = Vacancy('Full-Stack Developer', 'PHP', 'middle')
    V2 = Vacancy('C++ Developer', 'C++', 'middle')

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
    print(C1.full_name + ', main skill: ' + C1.main_skill)
    print(V1.title)
