# app\dashboard.py

import streamlit as st
import pandas as pd
import plotly.express as px

def show_dashboard():
    st.subheader("Dashboard")
    
    # Load data
    students_df = pd.read_excel("data/students.xlsx")
    staff_df = pd.read_excel("data/staffs.xlsx")
    grades_df = pd.read_excel("data/grades.xlsx")

     # Key Metrics - Displayed Vertically
    with st.container():
        st.metric("Total Students", len(students_df))
        st.metric("Total Staff", len(staff_df))
        st.metric("Total Grades Recorded", len(grades_df))

    # Visualizations
    st.markdown("### Students Enrollment Over Years")
    enrollment_chart = px.histogram(
        students_df, 
        x="current_class", 
        title="Student Enrollment by Class",
        color="current_class",  # Add color for better distinction
        template="plotly_white"  # Use a clean template
    )
    st.plotly_chart(enrollment_chart)

    st.markdown("### Grade Distribution")
    grade_chart = px.histogram(
        grades_df, 
        x="grade", 
        title="Grade Distribution",
        color="grade",  # Add color for better distinction
        template="plotly_white"
    )
    st.plotly_chart(grade_chart)

    st.markdown("### Staff by Department")
    department_chart = px.histogram(
        staff_df, 
        x="levels", 
        title="Staff Distribution by Levels",
        color="levels",  # Add color for better distinction
        template="plotly_white"
    )
    st.plotly_chart(department_chart)

    # Consider adding interactive filters here for further insights
    st.markdown("### Filters")
    # Example: filter by class or department
    selected_class = st.selectbox("Select Class", options=students_df['current_class'].unique())
    filtered_students = students_df[students_df['current_class'] == selected_class]
    st.write(filtered_students)  # Display filtered data

