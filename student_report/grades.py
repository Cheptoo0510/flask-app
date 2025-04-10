def calculate_average(grades):
    if not grades:
        return 0.0
    return sum(grades) / len(grades)
