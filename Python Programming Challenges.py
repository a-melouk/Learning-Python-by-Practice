# 1
def capital_indexes(string):
    result = []
    for i in range(len(string)):
        if string[i].isupper():
            result.append(i)
    return result


# 2
def middle_letter(string):
    if len(string) % 2 == 0:
        return ""
    else:
        temp = (len(string) - 1) / 2
        return string[int(temp)]


# 3
def online_count1(people):
    count = 0
    for status in people.values():
        if status == "online":
            count += 1
    return count


def online_count2(people):
    count = 0
    for name, status in people.items():
        if status == "online":
            count += 1
    return count


statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

# 4
import random


def random_number():
    return random.randint(1, 101)


# 5
def only_ints(a, b):
    if type(a) == type(b) and type(a) is int:
        return True


# 6
def double_letters(string):
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            return True
    return False


# 7
def add_dots(string):
    return ".".join(string)


def remove_dots(string):
    return string.replace(".", "")


# 8
def count(string):
    return string.count("-") + 1


# 9
def is_anagram(a, b):
    if len(a) != len(b):
        return False
    if sorted(a) == sorted(b):
        return True
    else:
        return False


# 10
def flatten(list):
    result = []
    for i in range(len(list)):
        for j in range(len(list[i])):
            result.append(list[i][j])
    print(result)
    return result


# 11
def largest_difference(list):
    sorted_list = sorted(list)
    return sorted_list[-1] - sorted_list[0]


# 12
def div_3(integer):
    if integer % 3 == 0:
        return True
    else:
        return False


# 13
def get_row_col(cell):
    temp = (".".join(cell)).split(".")
    print(temp)
    col = int(temp[1]) - 1
    row = ord(temp[0]) - 65
    return (col, row)


# 14
def palindrome(string):
    if len(string) % 2 == 1:
        middle_odd = int((len(string) - 1) / 2)
        if len(string) > middle_odd:
            string = string[:middle_odd] + string[middle_odd + 1 :]
    middle = (len(string)) / 2
    first_half = string[: int(middle)]
    second_half = string[int(middle) :]
    second_half = second_half[::-1]
    if first_half == second_half:
        return True
    else:
        return False


# 15
def up_down(number):
    return (number - 1, number + 1)


# 16
def consecutive_zeros(binary):
    return len(sorted(binary.split("1"))[-1])


# 17
def all_equal(array):
    temp = list(filter(lambda x: x != array[0], array))
    if len(temp) == 0:
        return True
    return False


# 18
def triple_and(bool1, bool2, bool3):
    if bool1 == bool2 == bool3 == True:
        return True
    return False


# 19
def convert(nums):
    return [str(num) for num in nums]


# 20
def zap(a, b):
    result = []
    for i in range(len(a)):
        result.append((a[i], b[i]))
    return result


zap([0, 1, 2, 3], [5, 6, 7, 8])


# 21
def validate(code):
    if code.find("def") == -1:
        return "missing def"
    if code.find(":") == -1:
        return "missing :"
    if code.find("(") == -1:
        return "missing paren"
    if code.find(")") == -1:
        return "missing paren"
    if code.find("()") == 1 or (code.find(")") - code.find("(") == 1):
        return "missing param"
    if code.find("    ") == -1:
        return "missing indent"
    if code.find("validate") == -1:
        return "wrong name"
    if code.find("return") == -1:
        return "missing return"
    return True


print(validate("def foo():\n print(123)"))
print(validate("def foo(x):\n print(123)"))
print(validate("def foo():\n print(123)"))


# 22
def list_xor(n, list1, list2):
    if n in list1 and n not in list2:
        return True
    if n not in list1 and n in list2:
        return True
    if n in list1 and n in list2:
        return False
    if n not in list1 and n not in list2:
        return False


print(list_xor(1, [1, 2, 3], [4, 5, 6]))
print(list_xor(1, [0, 2, 3], [1, 5, 6]))
print(list_xor(1, [1, 2, 3], [1, 5, 6]))
print(list_xor(1, [0, 0, 0], [4, 5, 6]))


# 23
def param_count(*args):
    return len(args)


# 24
def format_number(num):
    if len(str(num)) <= 3:
        return str(num)
    num = list(str(num))
    for i in range(len(num) - 3, 0, -3):
        num.insert(i, ",")
    return "".join(num)


print(format_number(123))
print(format_number(1234))
print(format_number(12345))
print(format_number(123456))
