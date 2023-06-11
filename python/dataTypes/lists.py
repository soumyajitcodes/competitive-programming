"""HackerRank Solutions"""

if __name__ == '__main__':
    N = int(input())

    numberList = []

    while N:
        cmd_List = list(input().split())

        if cmd_List[0] == "insert":
            numberList.insert(int(cmd_List[1]), int(cmd_List[2]))

        elif cmd_List[0] == "print":
            print(numberList)
        elif cmd_List[0] == "remove":
            numberList.remove(int(cmd_List[1]))
        elif cmd_List[0] == "append":
            numberList.append(int(cmd_List[1]))
        elif cmd_List[0] == "sort":
            numberList.sort()
        elif cmd_List[0] == "pop":
            numberList.pop()
        elif cmd_List[0] == "reverse":
            numberList.reverse()

        N -= 1
