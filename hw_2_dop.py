a = int(input('Введите число от 3 до 20: '))
pas = []
for i in range(a // 2):
    if a % 2 == 0:
        if i + 1 == a - i - 1:
            continue
        pas.append(i + 1)
        pas.append(a - i - 1)
    else:
        pas.append(i + 1)
        pas.append(a - i - 1)
print(pas)