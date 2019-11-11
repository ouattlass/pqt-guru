#  Copyright (c) 2019.
#  @Author : Lassina OUATTARA
#  @Python code


from models.Employe import Employee
import jsonpickle
import os


class EmployeeController:
    employee_list: list = []
    data_base = os.path.join(os.path.dirname(__file__), "..\\database\\Employees.json")

    @staticmethod
    def register_employee() -> None:
        EmployeeController.employee_list = EmployeeController.get_employee_list()
        EmployeeController.employee_list.append(Employee(employee_social_number=str(input('Social Number:')),
                                                         employee_name=str(input('Name: ')),
                                                         employee_surname=str(input('Surname: ')),
                                                         employee_gender=str(input('Sex: ')),
                                                         employee_birth_day=str(input('Birthday :')),
                                                         employee_phone_number=int(input('Phone number: ')),
                                                         employee_email=str(input('Email Address: ')),
                                                         employee_job_title=str(input('Title: ')),
                                                         employee_department=str(input('Department Code:'))))

        EmployeeController.save_list_in_file(EmployeeController.employee_list)

    @staticmethod
    def get_employee_list():
        if not EmployeeController.check_data_base():
            return
        else:
            with open(EmployeeController.data_base, 'r') as output_data:
                json_employee_list = output_data.read()
                employee_list = jsonpickle.decode(json_employee_list)
            return employee_list

    @staticmethod
    def get_employee(employee_code: str) -> Employee:
        employee_list = EmployeeController.get_employee_list()
        emp_socialNumber = EmployeeController.get_employee_social_code(employee_list)
        if employee_code in emp_socialNumber:
            for employee in employee_list:
                if employee['emp_social_number'] == employee_code:
                    print('employee trouver dans la base de donnee ...:)')
                return employee
        else:
            print('error... employee no trouver dans la base de donnee.. :(')

    @staticmethod
    def delete_employee(employee_code: str) -> None:
        employee_list = EmployeeController.get_employee_list()
        emp_socialNumber = EmployeeController.get_employee_social_code(employee_list)
        if employee_code in emp_socialNumber:
            for emp in employee_list:
                if emp['emp_social_number'] == employee_code:
                    employee_list.remove(emp)
                    EmployeeController.employee_list = employee_list
                if EmployeeController.save_list_in_file(employee_list):
                    print(F"employee with social number:{emp['emp_social_number']} have been removed ...:)")
        else:
            print('error... employee no trouver dans la base de donnee.. :(')

    @staticmethod
    def check_data_base() -> bool:
        if not os.path.isfile(EmployeeController.data_base) and not os.path.getsize(EmployeeController.data_base) > 0:
            return False
        else:
            return True

    @staticmethod
    def save_list_in_file(employee_list: list):
        print(employee_list)
        if EmployeeController.check_data_base():
            json_list = jsonpickle.encode(employee_list, unpicklable=False)
            with open(EmployeeController.data_base, 'w') as input_file:
                input_file.write(json_list)
            print('database updated....')
            return True
        else:
            return False

    @staticmethod
    def get_employee_social_code(employee_list) -> list:
        emp_social_number_list = []
        for employee in employee_list:
            emp_social_number_list.append(employee['emp_social_number'])
        return emp_social_number_list
