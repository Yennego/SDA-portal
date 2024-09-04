# app\classes.py

import streamlit as st
import pandas as pd

def manage_classes():
    st.subheader("Manage Classes")

    # Option to add a new class
    if st.button("Add New Class"):
        class_id = st.text_input("Class ID")
        class_name = st.text_input("Class Name")
        class_teacher = st.text_input("Class Teacher")
        grade_level = st.text_input("Grade Level")

        if st.button("Save"):
            new_class = {
                "classId": class_id,
                "className": class_name,
                "classTeacher": class_teacher,
                "gradeLevel": grade_level
            }
            df = pd.read_excel("data/classes.xlsx")
            df = df.append(new_class, ignore_index=True)
            df.to_excel("data/classes.xlsx", index=False)
            st.success("Class added successfully!")

    # Display all classes
    classes = pd.read_excel("data/classes.xlsx")
    st.dataframe(classes)

    # Option to update or delete a class
    if st.button("Update or Delete Class"):
        class_id = st.text_input("Enter Class ID to update or delete")
        action = st.selectbox("Action", ["Update", "Delete"])
        if action == "Update":
            class_name = st.text_input("Class Name")
            class_teacher = st.text_input("Class Teacher")
            grade_level = st.text_input("Grade Level")

            if st.button("Update"):
                df = pd.read_excel("data/classes.xlsx")
                df.loc[df['classId'] == class_id, ['className', 'classTeacher', 'gradeLevel']] = \
                    [class_name, class_teacher, grade_level]
                df.to_excel("data/classes.xlsx", index=False)
                st.success("Class updated successfully!")

        elif action == "Delete":
            if st.button("Delete"):
                df = pd.read_excel("data/classes.xlsx")
                df = df[df['classId'] != class_id]
                df.to_excel("data/classes.xlsx", index=False)
                st.success("Class deleted successfully!")
