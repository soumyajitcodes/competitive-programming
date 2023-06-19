import cmath

if __name__ == "__main__":
    complex_num = complex(input())

    r, p = cmath.polar(complex_num)

    print(r, p, sep="\n")