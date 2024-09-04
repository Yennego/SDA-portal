# app/services/student_service.py
import pandas as pd

def add_student(student_data, file_path="data/students.xlsx"):
    df = pd.read_excel(file_path)
    df = df.append(student_data, ignore_index=True)
    df.to_excel(file_path, index=False)

def get_students(file_path="data/students.xlsx"):
    return pd.read_excel(file_path)

def update_student(student_id, updated_data, file_path="data/students.xlsx"):
    df = pd.read_excel(file_path)
    df.loc[df['studentId'] == student_id, ['firstName', 'lastName', 'email', 'phoneNumber', 'enrollmentYear']] = \
        updated_data
    df.to_excel(file_path, index=False)

def delete_student(student_id, file_path="data/students.xlsx"):
    df = pd.read_excel(file_path)
    df = df[df['studentId'] != student_id]
    df.to_excel(file_path, index=False)
