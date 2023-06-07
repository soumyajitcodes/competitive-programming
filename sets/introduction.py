"""Introduction Set"""
def average(array):
    """Avg of Array"""
    # your code goes here
    setArray = set(array)

    avg = sum(setArray)/len(setArray)

    return "{:.3f}".format(round(avg, 3))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)