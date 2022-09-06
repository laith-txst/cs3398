# This function removes all even numbers from a given list
# Input: A list of ints
# Returns: A list of ints with all even numbers removed 
def remove_all_even_numbers_from_list(original_list):
    odd_number_list = [num for num in remaining_number_list if num % 2 != 0]
    return odd_number_list


one_to_ten_number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reversed_one_to_ten_number_list = list(reversed(one_to_ten_number_list))

for number in reversed_one_to_ten_number_list:
    if number != 3 and number != 7:
        print(f'{number} ', end = '')
print()

one_to_ten_set = set(reversed_one_to_ten_number_list)
one_to_ten_set.remove(8)
print(one_to_ten_set)

remaining_number_list = list(one_to_ten_set)
print(remaining_number_list)


# Remove all even numbers
odd_number_list = remove_all_even_numbers_from_list(remaining_number_list)
print(odd_number_list)
