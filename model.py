# model.py
import json
import mysql.connector


class Config:
    def __init__(self, config_path='config.json'):
        with open(config_path) as f:
            self.data = json.load(f)

    @property
    def background(self):
        return self.data['background']

    @property
    def primary_color(self):
        return self.data['primary_color']

    @property
    def secondary_color(self):
        return self.data['secondary']

    @property
    def third_color(self):
        return self.data['third']

    @property
    def fourth_color(self):
        return self.data['fourth']

    @property
    def software_version(self):
        return self.data['software_version']


class EmployeeModel:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='employee_db')

    def save_employee(self, employee_data):
        cursor = self.connection.cursor()
        query = "INSERT INTO employees (last_name, first_name, employee_id, location, shift) VALUES (%s, %s, %s, %s, %s)"
        values = (employee_data['last_name'], employee_data['first_name'], employee_data['employee_id'],
                  employee_data['location'], employee_data['shift'])
        cursor.execute(query, values)
        self.connection.commit()
        cursor.close()

    def save_bug_report(self, bug_report_data):
        cursor = self.connection.cursor()
        query = "INSERT INTO bug_reports (title, preconditions, description, expectation, reproducible, employee_id) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (bug_report_data['title'], bug_report_data['preconditions'], bug_report_data['description'],
                  bug_report_data['expectation'], bug_report_data['reproducible'], bug_report_data['employee_id'])
        cursor.execute(query, values)
        self.connection.commit()
        cursor.close()

    def get_employee_by_employee_id(self, employee_id):
        cursor = self.connection.cursor(dictionary=True)
        query = "SELECT * FROM employees WHERE employee_id = %s"
        values = (employee_id,)
        cursor.execute(query, values)
        employee = cursor.fetchone()
        cursor.close()
        return employee
