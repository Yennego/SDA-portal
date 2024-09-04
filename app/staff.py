# app\staff.py

import streamlit as st
import pandas as pd

def manage_staff():
    st.subheader("Manage Staff")

    # Option to add a new staff member
    with st.form("add_staff_form"):
        st.write("Add New Staff")
        staff_id = st.text_input("Staff ID")
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        email = st.text_input("Email")
        phone_number = st.text_input("Phone Number")
        levels = st.text_input("Level")
        role = st.text_input("Role")

        save_button = st.form_submit_button("Save")
        if save_button:
            new_staff = {
                "staffId": staff_id,
                "firstName": first_name,
                "lastName": last_name,
                "email": email,
                "phoneNumber": phone_number,
                "level": levels,
                "role": role
            }
            df = pd.read_excel("data/staffs.xlsx")
            df = df.append(new_staff, ignore_index=True)
            df.to_excel("data/staffs.xlsx", index=False)
            st.success("Staff member added successfully!")

    # Display all staff members
    staff = pd.read_excel("data/staffs.xlsx")
    st.dataframe(staff)

    # Option to update or delete a staff member
    if st.button("Update or Delete Staff"):
        with st.form("update_delete_staff_form"):
            staff_id = st.text_input("Enter Staff ID to update or delete")
            action = st.selectbox("Action", ["Update", "Delete"])

            if action == "Update":
                first_name = st.text_input("First Name")
                last_name = st.text_input("Last Name")
                email = st.text_input("Email")
                phone_number = st.text_input("Phone Number")
                levels = st.text_input("Level")
                role = st.text_input("Role")

                update_button = st.form_submit_button("Update")
                if update_button:
                    df = pd.read_excel("data/staffs.xlsx")
                    df.loc[df['staffId'] == staff_id, ['firstName', 'lastName', 'email', 'phoneNumber', 'level', 'role']] = \
                        [first_name, last_name, email, phone_number, levels, role]
                    df.to_excel("data/staffs.xlsx", index=False)
                    st.success("Staff member updated successfully!")

            elif action == "Delete":
                delete_button = st.form_submit_button("Delete")
                if delete_button:
                    df = pd.read_excel("data/staffs.xlsx")
                    df = df[df['staffId'] != staff_id]
                    df.to_excel("data/staffs.xlsx", index=False)
                    st.success("Staff member deleted successfully!")
