"""split & Join"""
def split_and_join(line):
    """split & Join"""
    return "-".join(line.split())

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
