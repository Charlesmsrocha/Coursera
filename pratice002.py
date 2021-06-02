def is_power_of_two(n):
    while n % 2 == 0 and n != 0:
        n = n / 2
    if n == 1:
        return True
    return False

print(is_power_of_two(0))
print(is_power_of_two(1))
print(is_power_of_two(8))
print(is_power_of_two(9))
    