import streamlit as st

import numpy as np
import face_recognition_models

def main():

    st.set_page_config(
        page_title="SnapClass - Making Attendance faster using AI",
        page_icon="https://i.ibb.co/YTYGn5qV/logo.png"
    )

    # Initialize login type
    if "login_type" not in st.session_state:
        st.session_state["login_type"] = None

    # -----------------------------------------
    # QR / Subject Link Enrollment
    # -----------------------------------------

    join_code = st.query_params.get("join-code")

    if join_code:

        # Force the user into Student portal
        if st.session_state.get("login_type") != "student":
            st.session_state["login_type"] = "student"
            st.rerun()

        # Student is logged in
        if (
            st.session_state.get("is_logged_in")
            and st.session_state.get("user_role") == "student"
        ):
            from src.components.dialog_auto_enroll import auto_enroll_dialog

            auto_enroll_dialog(join_code)
            return

    # -----------------------------------------
    # Normal Application Navigation
    # -----------------------------------------

    match st.session_state["login_type"]:

        case "teacher":
            from src.screen.teacher_screen import teacher_screen
            teacher_screen()

        case "student":
            from src.screen.student_screen import student_screen
            student_screen()

        case None:
            from src.screen.home_screen import home_screen
            home_screen()


if __name__ == "__main__":
    main()
