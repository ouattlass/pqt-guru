#  Copyright (c) 2019.
#  @Author : Lassina OUATTARA
#  @Python code
import datetime

from models.Department import Department


class Employee:

    def __init__(self, employee_social_number: str, employee_name: str,
                 employee_surname: str, employee_gender: str,
                 employee_birth_day: str, employee_phone_number: int,
                 employee_email: str, employee_job_title: str, employee_department: str):

        self.emp_social_number = employee_social_number
        self.emp_name = employee_name
        self.emp_surname = employee_surname
        self.emp_gender = employee_gender
        self.emp_birth_day = employee_birth_day
        self.emp_phone_number = employee_phone_number
        self.emp_email = employee_email
        self.emp_title = employee_job_title
        self.emp_department = employee_department
