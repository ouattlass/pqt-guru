#  Copyright (c) 2019.
#  @Author : Lassina OUATTARA
#  @Python code
from models.Department import Department
import os


class DepartmentController:
    department_list: list = []
    current_dir = os.path.dirname(__file__)

    @staticmethod
    def register_department(department: Department) -> None:
        pass

    @staticmethod
    def get_department_list() -> list:
        pass

    @staticmethod
    def delete_department(dep_code: str) -> None:
        pass

    @staticmethod
    def search_department(dep_code: str) -> Department:
        pass
