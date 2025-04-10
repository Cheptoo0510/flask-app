def calculate_attendance(attendance_list):
    if not attendance_list:
        return 0.0
    attended = sum(attendance_list)
    total_classes = len(attendance_list)
    return (attended / total_classes) * 100