"""Substring"""

def count_substring(string, sub_string):
    """substring"""

    sub_stringList = [string[i:j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)]

    substring_count = 0

    for str in sub_stringList:
        if str == sub_string:
            substring_count += 1

    return substring_count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
