if __name__ =="__main__":
    A = int(input())
    setA = set(map(int, input().split()[:A]))

    N = int(input())

    for _ in range(N):
        command = input().split()

        if command[0] == 'update':
            setA.update(map(int, input().split()[:int(command[1])]))
        elif command[0] == 'intersection_update':
            setA.intersection_update(map(int, input().split()[:int(command[1])]))
        elif command[0] == 'difference_update':
            setA.difference_update(map(int, input().split()[:int(command[1])]))
        elif command[0] == 'symmetric_difference_update':
            setA.symmetric_difference_update(map(int, input().split()[:int(command[1])]))

    print(sum(setA))
