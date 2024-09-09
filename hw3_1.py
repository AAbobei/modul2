calls = 0

def count_calls(calls):
    calls += 1
    return calls

def string_info(string):
    a = (len(string), string.lower(), string.upper)
    return a

print(string_info(string))