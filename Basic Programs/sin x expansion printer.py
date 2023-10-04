b = int(1)
for i in range(1, 9):
    b *= int(-1)
    a = 2 * i - 1
    if b != 1:
        c = "+"
    elif b == 1:
        c = "-"
    print(f"{c}x{a}", end=" ")
print("")
for i in range(1, 9):
    print(" --", end=" ")
print()
for i in range(1, 9):
    d = 2 * i - 1
    print(f" {d}!", end=" ")
