import streamlit as st
from app.dashboard import show_dashboard
from app.students import manage_students
from app.staff import manage_staff
from app.classes import manage_classes
from app.grades import manage_grades
from app.services.auth_service import authenticate_user

def login():
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    user_type = st.selectbox("Login as", ["Admin", "Staff", "Student"])

    if st.button("Login"):
        file_path = {
            "Admin": "data/admins.xlsx",
            "Staff": "data/staffs.xlsx",
            "Student": "data/students.xlsx"
        }[user_type]

        user = authenticate_user(file_path, username, password)
        if user:
            st.session_state["logged_in"] = True
            st.session_state["user"] = user
        else:
            st.error("Invalid username or password")
            st.session_state["logged_in"] = False
            
def logout():
    """Logout and clear the session state."""
    st.session_state['logged_in'] = False

def main():
    st.title("SDA School Portal")

    # Initialize session state for login status and user data
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
    if "user" not in st.session_state:
        st.session_state["user"] = None

    # Handle login
    if not st.session_state["logged_in"]:
        login()
        return  # Stop execution until login is successful

    # Safely access the user information after successful login
    user = st.session_state.get("user")
    if user is None:
        st.error("User information is missing. Please log in again.")
        st.session_state["logged_in"] = False  # Force re-login
        return

    st.sidebar.success(f"Welcome, {user['first_name']}!")
    st.sidebar.subheader("Navigation")
    page = st.sidebar.selectbox(
        "Select a page",
        ["Dashboard", "Students", "Staff", "Classes", "Grades"]
    )

    if page == "Dashboard":
        show_dashboard()
    elif page == "Students":
        manage_students()
    elif page == "Staff":
        manage_staff()
    elif page == "Classes":
        manage_classes()
    elif page == "Grades":
        manage_grades()
    else:
        st.error("Invalid page selected.")

    # Logout option
    if st.button("Logout"):
            logout()
    # else:
    #     login()

if __name__ == "__main__":
    main()
