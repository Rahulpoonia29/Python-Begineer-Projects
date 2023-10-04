def armstrong_number(number):
    temp_list = []
    sum_of_cube = 0
    power = len(str(number))

    for num in str(number):
        temp_list.append(num)
    # print(temp_list)

    for i_num in temp_list:
        sum_of_cube += int(i_num) ** power
    # print(sum)
    if sum_of_cube == number:
        return True


for i in range(1, 10000001):
    if armstrong_number(i):
        print(i)
