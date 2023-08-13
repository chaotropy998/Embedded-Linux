def count_number(lst, num):
    return lst.count(num)

lst = [1, 4, 3, 4, 4, 6, 4, 8, 9, 4, 10, 4, 4]
num = 4

print(f"Number {num} appeared {count_number(lst, num)} times in the given list.")