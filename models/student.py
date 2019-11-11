#  Copyright (c) 2019.
#  @Author : Lassina OUATTARA
#  @Python code

import datetime
from typing import List
import jsonpickle
import os


class Student:
    student_list: List = []
    student_database = os.path.join(os.path.dirname(__file__), "..\\database\\students.json")

    def __init__(self, name: str, surname: str, email: str, birthday: datetime.date):
        self.name = name
        self.surname = surname
        self.email = email
        self.dob = birthday
        Student.student_list.append(self)

    @staticmethod
    def save_to_file() -> None:
        json_object = jsonpickle.encode(Student.student_list, unpicklable=False)
        with open(Student.student_database, 'w') as output_file:
            output_file.write(json_object)

    @staticmethod
    def load_from_file() -> None:
        Student.student_list.clear()
        if not os.path.isfile(Student.student_database) \
                and not os.path.getsize(Student.student_database) > 0:
            return

        with open(Student.student_database, 'r') as datafile:
            json_object = datafile.read()
            student_list_dict = jsonpickle.decode(json_object)
            for student_dict in student_list_dict:
                Student(student_dict['name'],
                        student_dict['surname'],
                        student_dict['email'],
                        datetime.datetime.strptime(student_dict['dob'], '%Y-%m-%d').date())
