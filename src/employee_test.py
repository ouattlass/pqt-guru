#  Copyright (c) 2019.
#  @Author : Lassina OUATTARA
#  @Python code
from controller.EmployeeController import EmployeeController

if __name__ == '__main__':
    EmployeeController.register_employee()
    print(EmployeeController.get_employee_list())
    print(EmployeeController.get_employee('45789'))
    EmployeeController.delete_employee('45789')

