import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# ==========================================
# STUDENT PERFORMANCE DATA VISUALIZATION
# ==========================================

# Create student dataset
data = {
    "student_id": [1, 2, 3, 4, 5],
    "name": ["Ali", "Ahmed", "Sara", "Ayesha", "Hamza"],
    "gender": ["Male", "Male", "Female", "Female", "Male"],
    "age": [20, 21, 20, 22, 21],
    "study_hours": [4, 6, 5, 3, 7],
    "attendance": [85, 92, 95, 75, 98],
    "assignments": [80, 90, 94, 70, 95],
    "midterm": [72, 85, 91, 65, 90],
    "final_exam": [78, 88, 93, 68, 94]
}

# Convert data into DataFrame
df = pd.DataFrame(data)

# Save dataset as CSV
df.to_csv("student_performance.csv", index=False)

# ==========================================
# BASIC DATA ANALYSIS
# ==========================================

print("=" * 50)
print("STUDENT PERFORMANCE ANALYSIS")
print("=" * 50)

print("\nStudent Data:")
print(df)

print("\nAverage Marks:")
print("Assignments:", df["assignments"].mean())
print("Midterm:", df["midterm"].mean())
print("Final Exam:", df["final_exam"].mean())

print("\nHighest Final Exam Performer:")
highest = df.loc[df["final_exam"].idxmax()]
print(highest["name"], "-", highest["final_exam"])

print("\nLowest Final Exam Performer:")
lowest = df.loc[df["final_exam"].idxmin()]
print(lowest["name"], "-", lowest["final_exam"])

print("\nAverage Study Hours:")
print(df["study_hours"].mean())

print("\nAverage Attendance:")
print(df["attendance"].mean())

# ==========================================
# MATPLOTLIB VISUALIZATION 1
# Bar Chart - Final Marks
# ==========================================

plt.figure(figsize=(8, 5))
plt.bar(df["name"], df["final_exam"])
plt.title("Student Final Exam Marks")
plt.xlabel("Student")
plt.ylabel("Final Marks")
plt.tight_layout()
plt.savefig("1_final_marks_bar.png")
plt.show()

# ==========================================
# MATPLOTLIB VISUALIZATION 2
# Line Chart - Midterm vs Final
# ==========================================

plt.figure(figsize=(8, 5))
plt.plot(df["name"], df["midterm"], marker="o", label="Midterm")
plt.plot(df["name"], df["final_exam"], marker="o", label="Final Exam")
plt.title("Midterm vs Final Exam")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.legend()
plt.tight_layout()
plt.savefig("2_midterm_vs_final.png")
plt.show()

# ==========================================
# MATPLOTLIB VISUALIZATION 3
# Histogram - Final Exam Distribution
# ==========================================

plt.figure(figsize=(8, 5))
plt.hist(df["final_exam"], bins=5)
plt.title("Final Exam Marks Distribution")
plt.xlabel("Final Marks")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("3_final_exam_histogram.png")
plt.show()

# ==========================================
# SEABORN VISUALIZATION 4
# Study Hours vs Final Marks
# ==========================================

plt.figure(figsize=(8, 5))
sns.scatterplot(
    x="study_hours",
    y="final_exam",
    data=df,
    s=100
)
plt.title("Study Hours vs Final Marks")
plt.xlabel("Study Hours")
plt.ylabel("Final Marks")
plt.tight_layout()
plt.savefig("4_study_hours_vs_final.png")
plt.show()

# ==========================================
# SEABORN VISUALIZATION 5
# Attendance vs Final Marks
# ==========================================

plt.figure(figsize=(8, 5))
sns.scatterplot(
    x="attendance",
    y="final_exam",
    data=df,
    s=100
)
plt.title("Attendance vs Final Marks")
plt.xlabel("Attendance (%)")
plt.ylabel("Final Marks")
plt.tight_layout()
plt.savefig("5_attendance_vs_final.png")
plt.show()

# ==========================================
# SEABORN VISUALIZATION 6
# Correlation Heatmap
# ==========================================

plt.figure(figsize=(8, 6))

numeric_data = df[
    [
        "age",
        "study_hours",
        "attendance",
        "assignments",
        "midterm",
        "final_exam"
    ]
]

sns.heatmap(
    numeric_data.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Student Performance Correlation Heatmap")
plt.tight_layout()
plt.savefig("6_correlation_heatmap.png")
plt.show()

# ==========================================
# VISUALIZATION 7
# Assignments vs Final Marks
# ==========================================

plt.figure(figsize=(8, 5))
sns.scatterplot(
    x="assignments",
    y="final_exam",
    data=df,
    s=100
)
plt.title("Assignments vs Final Marks")
plt.xlabel("Assignment Marks")
plt.ylabel("Final Marks")
plt.tight_layout()
plt.savefig("7_assignments_vs_final.png")
plt.show()

# ==========================================
# VISUALIZATION 8
# Gender Performance
# ==========================================

gender_average = df.groupby("gender")["final_exam"].mean()

plt.figure(figsize=(7, 5))
gender_average.plot(kind="bar")
plt.title("Average Final Marks by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Final Marks")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("8_gender_performance.png")
plt.show()

# ==========================================
# PLOTLY INTERACTIVE DASHBOARD
# ==========================================

fig1 = px.bar(
    df,
    x="name",
    y="final_exam",
    title="Interactive Student Final Marks",
    hover_data=[
        "gender",
        "study_hours",
        "attendance",
        "assignments",
        "midterm"
    ]
)

fig1.show()

fig2 = px.scatter(
    df,
    x="study_hours",
    y="final_exam",
    size="attendance",
    color="gender",
    hover_name="name",
    title="Interactive Study Hours vs Final Marks"
)

fig2.show()

fig3 = px.scatter(
    df,
    x="attendance",
    y="final_exam",
    color="gender",
    hover_name="name",
    title="Interactive Attendance vs Final Marks"
)

fig3.show()

# ==========================================
# FINAL CONCLUSION
# ==========================================

study_final_correlation = df["study_hours"].corr(df["final_exam"])
attendance_final_correlation = df["attendance"].corr(df["final_exam"])

print("\n" + "=" * 50)
print("FINAL FINDINGS")
print("=" * 50)

print(
    f"\nCorrelation between study hours and final marks: "
    f"{study_final_correlation:.2f}"
)

print(
    f"Correlation between attendance and final marks: "
    f"{attendance_final_correlation:.2f}"
)

print("\nConclusion:")

if study_final_correlation > 0:
    print("Students who study more generally achieve higher final marks.")

if attendance_final_correlation > 0:
    print("Students with better attendance generally achieve higher final marks.")

print("\nProject completed successfully!")
