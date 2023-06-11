if __name__ == "__main__":
    sa = set(map(int, input().split()))
    for i in range(int(input())):
        s = set(map(int, input().split()))
        if not sa.issuperset(s):
            print("False")
            break
        else:
            print("True")
