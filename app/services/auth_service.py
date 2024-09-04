# app/services/auth_service.py
import pandas as pd

def authenticate_user(file_path, username, password):
    df = pd.read_excel(file_path)
    user = df[(df['username'] == username) & (df['password'] == password)]
    if not user.empty:
        return user.iloc[0].to_dict()
    return None
