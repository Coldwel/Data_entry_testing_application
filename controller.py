# controller.py

import tkinter as tk


class Controller:
    def __init__(self):
        from model import Config
        self.config = Config()

    def get_config(self):
        return {
            "background": self.config.background,
            "primary_color": self.config.primary_color,
            "secondary_color": self.config.secondary_color,
            "third_color": self.config.third_color,
            "fourth_color": self.config.fourth_color,
            "software_version": self.config.software_version
        }


class EmployeeController(Controller):
    def __init__(self):
        super().__init__()
        from model import EmployeeModel
        from main_ui import MainUserInterface, SecondWindow
        self.model = EmployeeModel()
        self.view = MainUserInterface()
        self.view.set_controller(self)
        self.second_window = SecondWindow(main_ui=self.view, controller=self)
        self.second_window.set_controller(self)

    def save_employee(self, employee_data):
        self.model.save_employee(employee_data)

    def control_report(self, bug_report_data):
        employee_id = bug_report_data["employee_id"]
        employee_data = {
            "last_name": bug_report_data["last_name"],
            "first_name": bug_report_data["first_name"],
            "employee_id": employee_id,
            "location": bug_report_data["location"],
            "shift": bug_report_data["shift"]
        }
        employee = self.model.get_employee_by_employee_id(employee_id)
        if employee:
            bug_report_data["employee_id"] = employee["id"]
            self.model.save_bug_report(bug_report_data)
        else:
            self.save_employee(employee_data)
            employee = self.model.get_employee_by_employee_id(employee_id)
            bug_report_data["employee_id"] = employee["id"]
            self.model.save_bug_report(bug_report_data)

    def run(self):
        self.view.main_window()
        tk.mainloop()
