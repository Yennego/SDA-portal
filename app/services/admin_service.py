# app/services/admin_service.py
import pandas as pd  # Third-party library import


def get_admins(file_path):
    return pd.read_excel(file_path)


def add_admin(admin_data, file_path):
    df = pd.read_excel(file_path)
    df = df.append(admin_data, ignore_index=True)
    df.to_excel(file_path, index=False)
