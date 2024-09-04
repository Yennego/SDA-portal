# app/models/student.py

import pandas as pd

class Staff:

    def __init__(self, staff_id, first_name, last_name, date_of_birth, email,
                 phone_number, position, levels, subjects_taught, username,
                 password, role):
        self.staff_id = staff_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone_number = phone_number
        self.position = position
        self.levels = levels
        self.subjects_taught = subjects_taught
        self.username = username
        self.password = password
        self.role = role

    def to_dict(self):
        return self.__dict__

def display_students():
    file_path = 'data/students.xlsx'
    return pd.read_excel(file_path)