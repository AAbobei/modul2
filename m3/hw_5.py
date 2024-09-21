def get_multiplied_digits(number):
    str_number = str(number)
    first = 1
    if len(str_number) == 1:
        if int(str_number) == 0:
            return first
        first = int(str_number)
        return first
    else:
        first = int(str_number[0])
        return first * get_multiplied_digits(int(str_number[1:]))


result = get_multiplied_digits(420)
print(result)