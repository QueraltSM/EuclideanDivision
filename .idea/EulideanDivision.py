def MCD_Euclides(a, b):
    while (b != 0):
        t = b;
        b = a % b;
        a = t;

    return a;


if __name__ == "__main__":
    print("Test 1: " + str(MCD_Euclides(60, 48)) + "\n")
    print("Test 2: " + str(MCD_Euclides(3768, 1727)) + "\n")
    print("Test 3 : " + str(MCD_Euclides(25, 5)))

    """
    Console results:

    Test 1: 12

    Test 2: 157

    Test 3 : 5

    Process finished with exit code 0

    """
    