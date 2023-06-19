import itertools

if __name__ == "__main__":
    io = list(input())

    for i, j in itertools.groupby(map(int, io)):
        print(tuple([len(list(j)), i]), end=" ")
