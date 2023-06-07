"""Symmetric difference"""

if __name__ == "__main__":
    M = int(input())
    MSet = set(int(i) for i in input().split()[:M])

    N = int(input())
    NSet = set(int(i) for i in input().split()[:N])

    MDifference = MSet.difference(NSet)
    NDifference = NSet.difference(MSet)
    MNUnion = sorted(MDifference.union(NDifference))

    for element in MNUnion:
        print(element)