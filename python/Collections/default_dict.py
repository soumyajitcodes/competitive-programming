import collections

if __name__ == "__main__":
    n, m = map(int, input().split())

    a=collections.defaultdict(list)
    for i in range(n):
        a[input()].append(i+1)

    for j in range(m+1):
        key = input()
        if len(a[key]) > 0:
            print(" ".join(str(c) for c in a[key]))
        else:
            print(-1)
