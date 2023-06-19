import itertools

if __name__ == "__main__":
    listA = list(map(int, input().split()))
    listB = list(map(int, input().split()))

    for element in itertools.product(listA, listB):
        print(element, end=" ")
