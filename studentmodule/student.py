def total(marks):
    return sum(marks)

def percentage(marks):
    return sum(marks) / len(marks)

def grade(p):
    if p >= 75:
        return "A"
    elif p >= 60:
        return "B"
    elif p >= 40:
        return "C"
    else:
        return "Fail"