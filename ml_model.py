import pandas as pd


def train_model():

    # Load student dataset
    df = pd.read_csv("data/students.csv")

    # Calculate academic score
    df["Academic_Score"] = (
        df["Python"]
        + df["Mathematics"]
        + df["Statistics"]
        + df["AI"]
        + df["ML"]
    ) / 5

    # Calculate predicted CGPA using
    # academic performance and attendance
    df["Predicted_CGPA"] = (
        (df["Academic_Score"] / 10) * 0.8
        + (df["Attendance"] / 100) * 2
    )

    return df


def predict_cgpa(model_data, student):

    # Calculate student's average subject mark
    average_marks = (
        student["Python"]
        + student["Mathematics"]
        + student["Statistics"]
        + student["AI"]
        + student["ML"]
    ) / 5

    # Calculate predicted CGPA
    predicted_cgpa = (
        (average_marks / 10) * 0.8
        + (student["Attendance"] / 100) * 2
    )

    # Keep CGPA within 0 to 10
    predicted_cgpa = max(0, min(10, predicted_cgpa))

    return predicted_cgpa