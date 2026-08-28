def calculate_stats(students):
    if len(students) == 0:
        return None

    total = 0
    max_score = 0
    min_score = 100
    max_student = ""
    min_student = ""

    for name, score in students.items():
        total += score

        if score > max_score:
            max_score = score
            max_student = name

        if score < min_score:
            min_score = score
            min_student = name

    avg = total / len(students)

    return {
        "average": avg,
        "max_score": max_score,
        "max_student": max_student,
        "min_score": min_score,
        "min_student": min_student,
    }
