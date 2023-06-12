if __name__ == "__main__":
    X = int(input())
    size_list = [int(i) for i in input().split()[:X]]
    N = int(input())
    shoe_size = []
    shoe_price = []
    while N:
        i, j = map(int, input().split())
        shoe_size.append(i)
        shoe_price.append(j)
        N -= 1

    money_earned = []
    for i in range(len(shoe_size)):
        if shoe_size[i] in size_list:
            money_earned.append(shoe_price[i])
            size_list.remove(shoe_size[i])
        else:
            money_earned.append(0)

    print(sum(money_earned))
