if __name__ == "__main__":
    n = int(input())
    s = set(map(int, input().split()))

    N = int(input())

    for _ in range(N):
        cmd = input().split()

        if cmd[0] == "discard":
            s.discard(int(cmd[1]))

        elif cmd[0] == "remove":
            s.remove(int(cmd[1]))

        elif cmd[0] == "pop":
            s.pop()

    print(sum(s))
