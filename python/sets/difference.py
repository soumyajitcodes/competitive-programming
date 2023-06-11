if __name__ == "__main__":
    n = int(input())
    english_news = set(map(int, input().split()[:n]))

    b = int(input())
    french_news = set(map(int, input().split()[:b]))

    print(len(english_news.difference(french_news)))
