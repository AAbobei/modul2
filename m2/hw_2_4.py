numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)):
    if numbers[i] == 1:
       continue
    j = 2
    for j in range(2, numbers[i]):
        if numbers[i] % j == 0:
           # if numbers[i] in not_primes:
            #    continue
            not_primes.append(numbers[i])
            break
        #if numbers[i] in primes:
         #   continue
    if numbers[i] not in not_primes:
        primes.append(numbers[i])
print(primes)
print(not_primes)