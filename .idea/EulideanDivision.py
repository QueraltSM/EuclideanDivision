def MCD_Euclides(a, b):
    while (b != 0):
        t = b;
        b = a % b;
        a = t;

    return a;


if __name__ == "__main__":
    print(MCD_Euclides(60, 48))
    print(MCD_Euclides(3768, 1727))
    print(MCD_Euclides(25, 5))