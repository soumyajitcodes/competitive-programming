if __name__ == '__main__':
    student_List = []

    for _ in range(int(input())):
        name = input()
        score = float(input())

        student_List.append([name, score])

    min_grade = float("inf")
    grade_list = []

    for entry in student_List:
        grade_list.append(entry[1])

    for grade in grade_list:
        if grade != min(grade_list) and grade < min_grade:
            min_grade = grade

    student_List.sort()

    for student in student_List:
        if student[1] == min_grade:
            print(student[0])
