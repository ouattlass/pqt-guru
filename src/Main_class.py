#!/usr/bin/env python3


"""PyCalc is a simple calculator built using Python and PyQt5."""

import sys
from functools import partial
          
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QGridLayout, QLineEdit, QMainWindow

from View.View_class import CalculatorView
from controller.Controllers import Controllers, ERROR_MSG

__version__ = '0.1'
__author__ = 'Lassina OUATTARA'


# Create a Model to handle the calculator's operation
def evaluateExpression(expression):
    """Evaluate an expression."""
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERROR_MSG

    return result


# Client code
def main():
    """Main function."""
    # Create an instance of QApplication
    python_calculator = QApplication(sys.argv)
    # Show the calculator's GUI
    view = CalculatorView()
    view.show()
    # Create instances of the model and the controller
    model = evaluateExpression
    Controllers(model=model, view=view)
    # Execute the calculator's main loop
    sys.exit(python_calculator.exec_())


if __name__ == '__main__':
    main()
