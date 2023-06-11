"""Tuples Solution"""

if __name__ == '__main__':
    N = int(input())

    arr = input().split()

    tuples = tuple(int(i) for i in arr)

    print(hash(tuples))
