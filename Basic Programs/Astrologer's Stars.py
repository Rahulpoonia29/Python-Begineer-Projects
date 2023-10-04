def top_to_down(row):
    temp_1 = 0
    temp_2 = row
    while temp_1 <= temp_2:
        for i in range(0, temp_1):
            print("*", end=" ")
        print()
        temp_1 += 1


def down_to_top(row):
    temp_3 = row
    while temp_3 > 0:
        for i in range(0, temp_3):
            print("*", end=" ")
        print()
        temp_3 -= 1


rows = int(input("Enter the number of rows to print "))
# rows = 5
mode = True
x = input("The current mode is top to bottom, do you want to change it (y/n) ")
# x = "y"

if x == "y":
    mode = False

if mode:
    top_to_down(rows)

else:
    down_to_top(rows)
