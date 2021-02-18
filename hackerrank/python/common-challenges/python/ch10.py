def gradingStudents(grades):

    rounded_grades = []

    for grade in grades:
        rounding = grade

        if grade < 38:
            rounded_grades.append(grade)
        else:
            next_mult = 0
            while (rounding % 5) != 0:
                next_mult += 1
                rounding += 1
            
            if next_mult < 3:
                rounded_grades.append(grade + next_mult)

            else:
                rounded_grades.append(grade)

    return rounded_grades   
