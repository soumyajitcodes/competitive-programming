from collections import namedtuple

if __name__ == "__main__":
    N = int(input())
    Student = namedtuple('Student', input().strip().split())
    print(sum(float(Student(*input().split()).MARKS) for _ in range(N)) / N)
