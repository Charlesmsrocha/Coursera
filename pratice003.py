def sum_divisors(n):
    sum = 0
    i = 1

    while n > 1:
        if n % i == 0:
            sum += i
            i += 1
        else:
            i += 1
    return sum

print(sum_divisors(0))
print(sum_divisors(3))
print(sum_divisors(36))
print(sum_divisors(102))
