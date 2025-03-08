import pandas as pd

attendance = pd.DataFrame(
    {
        "date": [
            "2020-01-01",
            "2020-01-01",
            "2020-01-01",
            "2020-01-02",
            "2020-01-02",
            "2020-01-02",
            "2020-01-03",
            "2020-01-03",
            "2020-01-03",
            "2020-01-03",
            "2020-01-03",
        ],
        "student_id": [1, 2, 3, 1, 2, 3, 1, 2, 3, 4, 5],
        "attendance": ["yes", "yes", "no", "no", "no", "no", "yes", "yes", "yes", "no", "yes"],
    }
)

students = pd.DataFrame(
    {
        "student_id": [1, 2, 3, 4, 5],
        "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
        "date_of_birth": ["2000-01-01", "2000-01-02", "2000-01-03", "2000-01-04", "2000-01-05"],
        "grade": ["grade 1", "grade 1", "grade 1", "grade 2", "grade 2"],
    }
)

attendance["date"] = pd.to_datetime(attendance["date"])
students["date_of_birth"] = pd.to_datetime(students["date_of_birth"])

merged = pd.merge(attendance, students, on="student_id")
total_students = students.shape[0]
attendance_on_birthday = merged[
    (merged["date"].dt.day == merged["date_of_birth"].dt.day)
    & (merged["date"].dt.month == merged["date_of_birth"].dt.month)
]["student_id"].nunique()

print(f"{attendance_on_birthday / total_students:2.2%} students attended class on their birthday")

attendance_by_day_and_grade = merged.groupby(["date", "grade"])["attendance"].value_counts().unstack().fillna(0)


compare_attendance = pd.merge(
    attendance_by_day_and_grade.loc["2020-01-03"],
    attendance_by_day_and_grade.loc["2020-01-02"],
    how="outer",
    on="grade",
    suffixes=("_2020-01-03", "_2020-01-02"),
).fillna(0)
compare_attendance["diff"] = compare_attendance["yes_2020-01-03"] - compare_attendance["yes_2020-01-02"]
compare_attendance.index[compare_attendance["diff"].argmin()]


compare_attendance.columns
