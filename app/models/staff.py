# app/models/staff.py
class Student:
    def __init__(self, student_id, first_name, last_name, date_of_birth, email, phone_number, age, current_level, current_class, section, username, password, role):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone_number = phone_number
        self.age = age
        self.current_level = current_level
        self.current_class = current_class
        self.section = section
        self.username = username
        self.password = password
        self.role = role

    def to_dict(self):
        return self.__dict__

