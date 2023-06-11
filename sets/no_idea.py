"""No Idea"""


def happiness(num_arr, A, B):
    """Happiness"""
    happiness = 0
    for i in num_arr:
        if i in A:
            happiness += 1
        elif i in B:
            happiness -= 1
        else:
            happiness += 0
    return happiness


if __name__ == "__main__":
    n, m = map(int, input().split())
    num_arr = [int(i) for i in input().split()[:n]]
    A = set(int(i) for i in input().split()[:m])
    B = set(int(i) for i in input().split()[:m])

    print(happiness(num_arr, A, B))
