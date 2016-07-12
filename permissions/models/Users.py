from models.Exams import Exams
from models.Tests import Tests
from models.Grades import Grades
from models.Attendance import Attendance
from db import database


roles = {
    "professor": {
        "exams": "rw",
        "tests": "rw",
        "grades": "rw",
        "attendance": "rw",
    },
    "teachers_assistant": {
        "exams": "r",
        "tests": "r",
        "grades": "rw",
        "attendance": "r",
    },
    "student": {
        "exams": "r",
        "tests": "r",
        "grades": "r",
        "attendance": "r",
    },
}

class User:

    def __init__(self, role, full_name): #dob, sex, school
        self.full_name = full_name
        self.role = role
        self.permissions = roles[role]
        ...
        #etc.
    
    @property
    def exams(self):
        if not hasattr(self, "_exams"):
            self._exams = Exams(self.permissions)
        return self._exams

    @property
    def tests(self):
        if not hasattr(self, "_tests"):
            self._tests = Tests(self.permissions)
        return self._tests

    @property
    def grades(self):
        if not hasattr(self, "_grades"):
            self._grades = Grades(self.permissions)
        return self._grades

    @property
    def attendance(self):
        if not hasattr(self, "_attendance"):
            self._attendance = Attendance(self.permissions)
        return self._attendance

