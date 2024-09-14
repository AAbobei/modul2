a = int(input('Введите число от 3 до 20: '))
pas1 = []
for i in range(1, a):
    for j in range(i + 1, a):
        if i + j  == a:
             pas1.append(i)
             pas1.append(j)
        elif  a % (i + j) == 0 :
            pas1.append(i)
            pas1.append(j)
print(pas1)
#a // (i + j) == j + i or