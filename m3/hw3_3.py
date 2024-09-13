def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

#1
print(print_params())
print(print_params(b = 25))
print(print_params(c = [1,2,3]))

#2
values_list = (13, '34', True)
values_dict = {'a': 1,
               'b': 'строка',
               'c': 25}
print(print_params(*values_list))
print(print_params(**values_dict))

#3
values_list_2 = (1, 2)
print(print_params(*values_list_2, 42))