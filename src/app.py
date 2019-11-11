#  Copyright (c) 2019.
#  @Author : Lassina OUATTARA
#  @Python code
import sys
import re
from PyQt5.Qt import QDate
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QHeaderView, QMessageBox
from View.Student_UI import Ui_fenetre
from models.student import Student


class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_fenetre()
        self.ui.setupUi(self)
        self.build_ui()
        self.show()
        self._error_message = ""

    def build_ui(self) -> None:
        self.ui.add_button.clicked.connect(self.add_student)

        self.ui.clear_button.clicked.connect(self.clear_form)
        self.ui.delete_button.clicked.connect(self.delete_student)
        self.ui.tableau.setColumnCount(4)
        self.ui.tableau.setHorizontalHeaderLabels(('Name', 'Surname', 'Email', 'DOB'))
        self.ui.tableau.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.load_students()

    def load_students(self) -> None:
        for i in reversed(range(self.ui.tableau.rowCount())):
            self.ui.tableau.removeRow(i)

        Student.load_from_file()
        row_pos = 0
        for student in Student.student_list:
            self.ui.tableau.insertRow(row_pos)
            self.ui.tableau.setItem(row_pos, 0, QTableWidgetItem(student.name))
            self.ui.tableau.setItem(row_pos, 1, QTableWidgetItem(student.surname))
            self.ui.tableau.setItem(row_pos, 2, QTableWidgetItem(student.email))
            self.ui.tableau.setItem(row_pos, 3, QTableWidgetItem(student.dob.strftime('%Y-%m-%d')))
            row_pos += 1

    def is_valid_input(self) -> bool:
        is_valid = True

        if not self.ui.name_input.text():
            self._error_message += "<h3>Student name is missing.\n</h3>"
            is_valid = False
        if not self.ui.surname_input.text():
            self._error_message += "<h3>Student surname is missing.\n</h3>"
            is_valid = False
        if not self.ui.email_input.text():
            self._error_message += "<h3>Student email is missing.\n</h3>"
            is_valid = False
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", self.ui.email_input.text()):
            self._error_message += "<h3>Email address is invalid.\n</h3>"
            is_valid = False
        return is_valid

    def add_student(self) -> None:
        if not self.is_valid_input():
            msg = QMessageBox()

            msg.setIcon(QMessageBox.Critical)
            msg.setText(self._error_message)
            msg.setWindowTitle("Error in entry")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            self._error_message = ""
            return
        name = self.ui.name_input.text()
        surname = self.ui.surname_input.text()
        email = self.ui.email_input.text()
        dob = self.ui.calendar.selectedDate().toPyDate()
        Student(name, surname, email, dob)
        Student.save_to_file()
        self.clear_form()
        self.load_students()

    def clear_form(self) -> None:
        self.ui.name_input.clear()
        self.ui.surname_input.clear()
        self.ui.email_input.clear()
        self.ui.calendar.setSelectedDate(QDate.currentDate())

    def delete_student(self) -> None:
        rows = sorted(set(index.row() for index in
                          self.ui.tableau.selectedIndexes()))

        if len(rows) < 1:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("<h2>Please select a student to delete</h2>")
            msg.setWindowTitle("No Student Selected")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return
        ask = QMessageBox()
        ask.setIcon(QMessageBox.Question)
        ask.setText("<h2>Are you sure you want to delete this student?</h2>")
        ask.setWindowTitle("Really Delete Student?")
        ask.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        ask.activateWindow()
        ret_val = ask.exec_()
        if ret_val == QMessageBox.No:
            return
        for row in rows:
            Student.student_list.pop(row)
            Student.save_to_file()
            self.load_students()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())
