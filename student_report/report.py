from grades import calculate_average
from attendance import calculate_attendance

def generate_report(grades, attendance):
    avg_grade = calculate_average(grades)
    attendance_percent = calculate_attendance(attendance)

    print("📊 Student Performance Report")
    print("-" * 30)
    print(f"Average Grade: {avg_grade:.2f}")
    print(f"Attendance: {attendance_percent:.2f}%")
    print("-" * 30)



if __name__ == "__main__":
    sample_grades = [85, 90, 78, 92, 88]
    sample_attendance = [1, 1, 0, 1, 1, 1, 0]

    generate_report(sample_grades, sample_attendance)
