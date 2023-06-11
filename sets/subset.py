if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        countA = int(input())
        setA = set(map(int, input().split()[:countA]))

        countB = int(input())
        setB = set(map(int, input().split()[:countB]))

        print(setA.issubset(setB))
