def get_multiplied_digits(number):
    str_number = str(number)
    first = 1
    if len(str_number) == 1:
        first = int(str_number)
        return first
    else:
        first = int(str_number[0])
        return first * get_multiplied_digits(int(str_number[1:]))

result = get_multiplied_digits(40203)
print(result)