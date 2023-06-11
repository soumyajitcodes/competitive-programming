if __name__ == '__main__':
    t = int(input())
    students = []
    for i in range(t):
        n, m1, m2, m3 = input().split()
        student = [n, float(m1), float(m2), float(m3)]
        students.append(student)
    N = input()
    for a, b, c, d in students:
        if a == N:
            avg = float((b + c + d) / 3)
    print("{:.2f}".format(round(avg, 2)))
