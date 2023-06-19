import itertools

if __name__ == "__main__":
    S, k = input().split()
    S = sorted(S)
    k = int(k)

    for element in itertools.combinations_with_replacement(S, k):
        print(''.join(element))