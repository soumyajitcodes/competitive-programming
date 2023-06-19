import itertools

if __name__ == "__main__":
    string = input().split()

    string_permutations = list(itertools.permutations(string[0], int(string[1])))
    string_permutations.sort()

    for element in string_permutations:
        print("".join(element))