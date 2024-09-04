# app/services/grade_service.py
import pandas as pd

def get_grades(file_path):
    return pd.read_excel(file_path)

def add_grade(grade_data, file_path):
    df = pd.read_excel(file_path)
    df = df.append(grade_data, ignore_index=True)
    df.to_excel(file_path, index=False)
