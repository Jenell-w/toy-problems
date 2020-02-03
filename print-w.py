def make_w(height):
    i = 0
    j = height - 1
    for row in range(height):
        for col in range(height+3):
            # if col == 0 or (col == height + 2) or (col == height + 1 and row == height - 2) or (col == height and row == height-3):
            if col == 0 or (col == height + 2) or (row+col == height - 1) or (col-row == height - 1):
                print("* ", end="")
            elif row == i and col == j:
                print("*", end="")
                i += 2
                j -= 2
            else:
                print(end=" ")

        print()


make_w(5)
# program prints (need to fix the first if statement, the last column is not right):
# *    *   *
# *   *  *  *
# *  *    * *
# * *      *
# *       *
