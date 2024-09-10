calls = 0

def count_calls():
    global calls
    calls += 1
    return calls

def string_info(string):
    a = (len(string), string.lower(), string.upper())
    count_calls()
    return a

def is_contains(string, list_to_search):
    count_calls()
    for i in range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].upper()
    if string.upper() in list_to_search:
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(string_info('AdfwerfSAEF'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)