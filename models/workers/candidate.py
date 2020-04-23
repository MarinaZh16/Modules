"""module that holds class Candidate"""
from csv import DictReader


class Candidate(object):
    """class that holds job candidate data"""
    def __init__(self, full_name, email, technologies, main_skill,
                 main_skill_grade):
        self.full_name = full_name
        self.email = email
        self.technologies = technologies
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    @property
    def info(self):
        return '%s, %s, %s, %s, %s' % (self.full_name, self.email, self.technologies,
                                       self.main_skill, self.main_skill_grade)

    @classmethod
    def from_csv(cls, fp):
        obj_list = []
        with open(fp, 'r') as f:
            file_data = [row for row in DictReader(f)]
        for row in file_data:
            full_name = row['\ufeffFull Name']
            email = row['Email']
            technologies = row['Technologies'].split('|')
            main_skill = row['Main Skill']
            main_skill_grade = row['Main Skill Grade']
            obj_list.append(cls(full_name=full_name,
                                email=email,
                                technologies=technologies,
                                main_skill=main_skill,
                                main_skill_grade=main_skill_grade))
        return obj_list


