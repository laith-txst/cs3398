one_to_ten_number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reversed_one_to_ten_number_list = list(reversed(one_to_ten_number_list))

for number in reversed_one_to_ten_number_list:
    if number != 3 and number != 7:
        print(number, end = '')
print()

one_to_ten_set = set(reversed_one_to_ten_number_list)
one_to_ten_set.remove(8)
print(one_to_ten_set)
