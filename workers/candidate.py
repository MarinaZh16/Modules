"""module that holds class Candidate"""
class Candidate(object):
    """class that holds job candidate data"""
    def __init__(self, full_name, email, technologies, main_skill,
                 main_skill_grade):
        self.full_name = full_name
        self.email = email
        self.technologies = technologies
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade
