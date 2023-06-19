import collections

if __name__ == "__main__":
    N = int(input())

    item_dict = collections.OrderedDict()

    for _ in range(N):
        item_element = input().split()
        item_price = int(item_element[-1])
        item_name = " ".join(item_element[:-1])

        if item_name not in item_dict:
            item_dict[item_name] = item_price
        else:
            item_dict[item_name] += item_price

    for key in item_dict.keys():
        print(key, item_dict[key])
