
'''Old way'''
# numbers = [1,2,3]
# new_list = []
# for n in numbers:
#     add_1 = n+1
#     new_list.append(add_1)

'''Python Sequences: list, range, string, tuple'''

'''Using list comprehension'''
'''new_list = [new_item for item in numbers]'''
# new_list = [n+1 for n in numbers]
# print(new_list)

# name = "Angela"
# new_list = [letter for letter in name]
# print(new_list)

# new_list = [num*2 for num in range(1,5)]
# print(new_list)

'''Conditional List Comprehension'''
'''new_list = [new_item for item in item_list if condition]'''
# names_list = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names_list = [name for name in names_list if len(name)<5]
# print(short_names_list)
# long_names_list = [name.upper() for name in names_list if len(name)>5]
# print(long_names_list)
'''only even numbers'''
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# even_numbers_list = [num for num in numbers if num%2==0]
# print(even_numbers_list)

'''result which contains the numbers that are common in both files.'''
result = []
with open("file1.txt") as file1_data:
    file1 = file1_data.readlines()
with open("file2.txt") as file2_data:
    file2 = file2_data.readlines()
result = [int(num) for num in file1 if num in file2]
print(result)

