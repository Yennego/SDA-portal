# app\students.py

import streamlit as st
import pandas as pd

def manage_students():
    st.subheader("Manage Students")

    # Option to add a new student
    if st.button("Add New Student"):
        st.session_state['show_add_form'] = True

    if 'show_add_form' in st.session_state and st.session_state['show_add_form']:
        with st.form(key="add_student_form"):
            student_id = st.text_input("Student ID")
            first_name = st.text_input("First Name")
            last_name = st.text_input("Last Name")
            email = st.text_input("Email")
            phone_number = st.text_input("Phone Number")
            date_of_birth = st.text_input("Date of Birth (YYYY-MM-DD)", placeholder="e.g., 2005-01-01")

            save_button = st.form_submit_button("Save")
            if save_button:
                new_student = pd.DataFrame({
                    "studentId": [student_id],
                    "first_name": [first_name],
                    "last_name": [last_name],
                    "dateOfBirth": [date_of_birth],
                    "email": [email],
                    "phoneNumber": [phone_number],
                    "age": [None],
                    "current_level": [None],
                    "current_class": [None],
                    "section": [None],
                    "username": [None],
                    "password": [None],
                    "role": ["student"],
                    "is_active": [True],
                    "date_created": [pd.Timestamp.now()]
                })

                try:
                    df = pd.read_excel("data/students.xlsx")
                except Exception as e:
                    st.error(f"Error reading Excel file: {e}")
                    return

                if not all(col in df.columns for col in new_student.columns):
                    st.error("Column mismatch between existing data and new data.")
                    return

                try:
                    df = pd.concat([df, new_student], ignore_index=True)
                    df.to_excel("data/students.xlsx", index=False)
                    st.success("Student added successfully!")
                    st.session_state['show_add_form'] = False
                except Exception as e:
                    st.error(f"Error saving Excel file: {e}")

    # Display all students
    try:
        students = pd.read_excel("data/students.xlsx")
        st.dataframe(students)
    except Exception as e:
        st.error(f"Error displaying students: {e}")

    # Option to update or delete a student
    if st.button("Update or Delete Student"):
        st.session_state['show_update_form'] = True

    if 'show_update_form' in st.session_state and st.session_state['show_update_form']:
        with st.form(key="update_student_form"):
            student_id = st.text_input("Enter Student ID to update or delete")
            action = st.selectbox("Action", ["Update", "Delete"])

            if action == "Update":
                first_name = st.text_input("First Name")
                last_name = st.text_input("Last Name")
                email = st.text_input("Email")
                phone_number = st.text_input("Phone Number")
                date_of_birth = st.text_input("Date of Birth (YYYY-MM-DD)")

                update_button = st.form_submit_button("Update")
                if update_button:
                    try:
                        df = pd.read_excel("data/students.xlsx")
                        df.loc[df['studentId'] == student_id, 
                               ['first_name', 'last_name', 'dateOfBirth', 'email', 'phoneNumber']] = \
                            [first_name, last_name, date_of_birth, email, phone_number]
                        df.to_excel("data/students.xlsx", index=False)
                        st.success("Student updated successfully!")
                        st.session_state['show_update_form'] = False
                    except Exception as e:
                        st.error(f"Error updating student: {e}")

            elif action == "Delete":
                delete_button = st.form_submit_button("Delete")
                if delete_button:
                    try:
                        df = pd.read_excel("data/students.xlsx")
                        df = df[df['studentId'] != student_id]
                        df.to_excel("data/students.xlsx", index=False)
                        st.success("Student deleted successfully!")
                        st.session_state['show_update_form'] = False
                    except Exception as e:
                        st.error(f"Error deleting student: {e}")
