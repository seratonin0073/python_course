def task1_len(string):
    return len(string)

def task1_join(string1, string2):
    return ''.join([string1, string2])

def task2_squre(num):
    return num ** 2

def task2_sum(num1, num2):
    return num1 + num2

def task2_division(num1, num2):
    return divmod(num1, num2)

def task3_avg(num_list):
    return sum(num_list) / len(num_list)

def task3_intersection(list1, list2):
    return list(set(list1) & set(list2))

def task4_keys(dictionary):
    return list(dictionary.keys())

def task4_join_dict(dict1, dict2):
    return dict1 | dict2

def task5_union(set1, set2):
    return set1 | set2

def task5_is_subset(set1, set2):
    return set1.issubset(set2)

def task6_even_odd_number(num):
    return "Even" if num % 2 == 0 else "Odd"

def task6_even_list(num_list):
    return [num for num in num_list if num % 2 == 0]

print(f"{'=' * 10} Task 1 {'=' * 10}")
print(task1_len("Hello, World!"))
print(task1_join("Hello, ", "World!"))

print(f"\n{'=' * 10} Task 2 {'=' * 10}")
print(task2_squre(5))
print(task2_sum(10, 20))
print(task2_division(10, 3))

print(f"\n{'=' * 10} Task 3 {'=' * 10}")
print(task3_avg([1, 2, 3, 4, 5]))
print(task3_intersection([1, 2, 3], [2, 3, 4]))

print(f"\n{'=' * 10} Task 4 {'=' * 10}")
print(task4_keys({"a": 1, "b": 2, "c": 3}))
print(task4_join_dict({"a": 1, "b": 2}, {"c": 3, "d": 4}))  

print(f"\n{'=' * 10} Task 5 {'=' * 10}")
print(task5_union({1, 2, 3}, {3, 4, 5}))
print(task5_is_subset({1, 2}, {1, 2, 3}))

print(f"\n{'=' * 10} Task 6 {'=' * 10}")
print(task6_even_odd_number(10))
print(task6_even_odd_number(11))
print(task6_even_list([1, 2, 3, 4, 5, 6]))

print(f"\n{'=' * 10} Task 7 {'=' * 10}")
is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(is_even(10))
print(is_even(11))