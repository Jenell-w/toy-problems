def make_w(height):
    i = height-1
    j = 1
    for i in range(height-1, -1, -1):
        for j in range(height-1, i, -1):
            print("-", end="")
        for j in range(height-2, 2, -1):
            print("*", end="")
        for j in range(1, i*2, 1):
            print("-", end="")
        for j in range(-1, -1, 1):
            print("0", end="")
        for j in range(height-1, -1, 1):
            print("-", end="")
        print("8", end="")

        if (i >= 1):
            print("*", end="")
        print()


make_w(5)
