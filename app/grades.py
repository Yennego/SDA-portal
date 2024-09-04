# app\grades.py

import streamlit as st
import pandas as pd

def manage_grades():
    st.subheader("Manage Grades")

    # Option to add a new grade
    if st.button("Add New Grade"):
        student_id = st.text_input("Student ID")
        subject_id = st.text_input("Subject ID")
        staff_id = st.text_input("Staff ID")
        score = st.number_input("Score", min_value=0.0, max_value=100.0)
        grade = st.text_input("Grade")
        term = st.text_input("Term")
        academic_year = st.text_input("Academic Year")

        if st.button("Save"):
            new_grade = {
                "studentId": student_id,
                "subjectId": subject_id,
                "staffId": staff_id,
                "score": score,
                "grade": grade,
                "term": term,
                "academicYear": academic_year,
                "dateRecorded": pd.Timestamp.now().isoformat()
            }
            df = pd.read_excel("data/grades.xlsx")
            df = df.append(new_grade, ignore_index=True)
            df.to_excel("data/grades.xlsx", index=False)
            st.success("Grade added successfully!")

    # Display all grades
    grades = pd.read_excel("data/grades.xlsx")
    st.dataframe(grades)

    # Option to update or delete a grade
    if st.button("Update or Delete Grade"):
        student_id = st.text_input("Enter Student ID to update or delete")
        subject_id = st.text_input("Enter Subject ID to update or delete")
        action = st.selectbox("Action", ["Update", "Delete"])
        if action == "Update":
            score = st.number_input("Score", min_value=0.0, max_value=100.0)
            grade = st.text_input("Grade")
            term = st.text_input("Term")
            academic_year = st.text_input("Academic Year")

            if st.button("Update"):
                df = pd.read_excel("data/grades.xlsx")
                df.loc[(df['studentId'] == student_id) & (df['subjectId'] == subject_id), 
                       ['score', 'grade', 'term', 'academicYear']] = \
                    [score, grade, term, academic_year]
                df.to_excel("data/grades.xlsx", index=False)
                st.success("Grade updated successfully!")

        elif action == "Delete":
            if st.button("Delete"):
                df = pd.read_excel("data/grades.xlsx")
                df = df[~((df['studentId'] == student_id) & (df['subjectId'] == subject_id))]
                df.to_excel("data/grades.xlsx", index=False)
                st.success("Grade deleted successfully!")
