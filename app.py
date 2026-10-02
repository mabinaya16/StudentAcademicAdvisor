import streamlit as st
import pandas as pd

from ml_model import train_model, predict_cgpa


# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Student Academic Advisor",
    page_icon="🎓",
    layout="wide"
)


# =====================================================
# TITLE
# =====================================================

st.title("🎓 AI-Based Student Academic Advisor")

st.write(
    "Academic Performance and Course Recommendation Agent"
)

st.divider()


# =====================================================
# LOAD DATASET
# =====================================================

try:

    df = pd.read_csv("data/students.csv")

except FileNotFoundError:

    st.error("students.csv file not found.")

    st.info(
        "Make sure students.csv is inside the data folder."
    )

    st.stop()


# =====================================================
# CREATE MODEL DATA
# =====================================================

model_data = train_model()


# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.header("🎓 Student Profile")

student_name = st.sidebar.selectbox(
    "Select Student",
    df["Name"].tolist()
)


# =====================================================
# SELECT STUDENT
# =====================================================

student = df[
    df["Name"] == student_name
].iloc[0]


# =====================================================
# AI CGPA PREDICTION
# =====================================================

predicted_cgpa = predict_cgpa(
    model_data,
    student
)


# =====================================================
# STUDENT INFORMATION
# =====================================================

st.header("👤 Student Information")

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Student Name",
        student["Name"]
    )

with col2:

    st.metric(
        "Department",
        student["Department"]
    )

with col3:

    st.metric(
        "Semester",
        student["Semester"]
    )

with col4:

    st.metric(
        "Current CGPA",
        f'{student["CGPA"]:.2f}'
    )


# =====================================================
# ACADEMIC PERFORMANCE
# =====================================================

st.header("📊 Academic Performance")

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Attendance",
        f'{student["Attendance"]}%'
    )

with col2:

    st.metric(
        "Python",
        student["Python"]
    )

with col3:

    st.metric(
        "Mathematics",
        student["Mathematics"]
    )


col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Statistics",
        student["Statistics"]
    )

with col2:

    st.metric(
        "Artificial Intelligence",
        student["AI"]
    )

with col3:

    st.metric(
        "Machine Learning",
        student["ML"]
    )


# =====================================================
# SUBJECT PERFORMANCE
# =====================================================

st.header("📈 Subject Performance")

subjects = [
    "Python",
    "Mathematics",
    "Statistics",
    "AI",
    "ML"
]

marks = [
    student["Python"],
    student["Mathematics"],
    student["Statistics"],
    student["AI"],
    student["ML"]
]

chart_data = pd.DataFrame(
    {
        "Subject": subjects,
        "Marks": marks
    }
)

st.bar_chart(
    chart_data.set_index("Subject")
)


# =====================================================
# AI PERFORMANCE PREDICTION
# =====================================================

st.header("🤖 AI Performance Prediction")

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Current CGPA",
        f'{student["CGPA"]:.2f}'
    )

with col2:

    st.metric(
        "Predicted CGPA",
        f"{predicted_cgpa:.2f}"
    )


if predicted_cgpa >= student["CGPA"]:

    st.success(
        "📈 The academic indicators show potential for improvement."
    )

else:

    st.warning(
        "📚 Continue improving your subject performance and attendance."
    )


# =====================================================
# STRONG AND WEAK SUBJECTS
# =====================================================

st.header("💪 Academic Analysis")

subject_marks = {

    "Python": student["Python"],

    "Mathematics": student["Mathematics"],

    "Statistics": student["Statistics"],

    "Artificial Intelligence": student["AI"],

    "Machine Learning": student["ML"]

}


strong_subjects = []

weak_subjects = []


for subject, mark in subject_marks.items():

    if mark >= 80:

        strong_subjects.append(subject)

    if mark < 60:

        weak_subjects.append(subject)


col1, col2 = st.columns(2)


# Strong subjects

with col1:

    st.subheader("💪 Strong Subjects")

    if strong_subjects:

        for subject in strong_subjects:

            st.success(subject)

    else:

        st.info(
            "No strong subjects found."
        )


# Weak subjects

with col2:

    st.subheader("📚 Subjects to Improve")

    if weak_subjects:

        for subject in weak_subjects:

            st.warning(subject)

    else:

        st.info(
            "No major weak subjects."
        )


# =====================================================
# COURSE RECOMMENDATION
# =====================================================

st.header("🎯 Recommended Courses")

recommendations = []


if student["Python"] >= 80:

    recommendations.append(
        "Data Science"
    )


if student["AI"] >= 80:

    recommendations.append(
        "Machine Learning"
    )


if student["ML"] >= 80:

    recommendations.append(
        "Deep Learning"
    )


if student["Statistics"] >= 80:

    recommendations.append(
        "Data Analytics"
    )


if student["Mathematics"] >= 80:

    recommendations.append(
        "Advanced Algorithms"
    )


if recommendations:

    for course in recommendations:

        st.success(
            "🎓 Recommended: " + course
        )

else:

    st.info(
        "Improve your academic performance "
        "before taking advanced courses."
    )


# =====================================================
# ACADEMIC ADVISOR
# =====================================================

st.header("🤖 AI Academic Advisor")

advice = []


if student["Python"] < 60:

    advice.append(
        "Improve your Python programming fundamentals."
    )


if student["Mathematics"] < 60:

    advice.append(
        "Spend more time practicing Mathematics."
    )


if student["Statistics"] < 60:

    advice.append(
        "Practice Statistics concepts regularly."
    )


if student["AI"] < 60:

    advice.append(
        "Study basic Artificial Intelligence concepts."
    )


if student["ML"] < 60:

    advice.append(
        "Strengthen your Machine Learning fundamentals."
    )


if student["Attendance"] < 75:

    advice.append(
        "Try to improve your class attendance."
    )


if student["CGPA"] >= 8.5:

    advice.append(
        "Your academic performance is strong. "
        "Consider advanced learning opportunities."
    )


if not advice:

    advice.append(
        "Maintain your current performance "
        "and continue learning."
    )


for message in advice:

    st.info(
        "💡 " + message
    )


# =====================================================
# OVERALL PERFORMANCE
# =====================================================

st.header("🏆 Overall Performance")

cgpa = float(
    student["CGPA"]
)


if cgpa >= 8.5:

    st.success(
        "🌟 Excellent Academic Performance"
    )

elif cgpa >= 7.0:

    st.info(
        "👍 Good Academic Performance"
    )

elif cgpa >= 6.0:

    st.warning(
        "⚠️ Average Academic Performance"
    )

else:

    st.error(
        "📚 Academic performance needs improvement."
    )


# =====================================================
# ATTENDANCE STATUS
# =====================================================

st.header("📅 Attendance Status")

attendance = float(
    student["Attendance"]
)


if attendance >= 85:

    st.success(
        f"Attendance: {attendance}% - Good Attendance"
    )

elif attendance >= 75:

    st.warning(
        f"Attendance: {attendance}% - Monitor Attendance"
    )

else:

    st.error(
        f"Attendance: {attendance}% - Low Attendance"
    )


# =====================================================
# SELECTED STUDENT DETAILS
# =====================================================

st.header("📋 Selected Student Details")

selected_data = pd.DataFrame(
    [student]
)

st.dataframe(
    selected_data,
    use_container_width=True
)


# =====================================================
# COMPLETE DATASET
# =====================================================

st.header("📚 Complete Student Dataset")

st.dataframe(
    df,
    use_container_width=True
)


# =====================================================
# PROJECT INFORMATION
# =====================================================

st.divider()

st.subheader("📌 About This Project")

st.write(
    "This system analyzes student academic performance "
    "using Python and provides CGPA prediction, "
    "course recommendations and personalized "
    "academic advice."
)

st.caption(
    "AI-Based Student Academic Advisor and "
    "Course Recommendation Agent"
)