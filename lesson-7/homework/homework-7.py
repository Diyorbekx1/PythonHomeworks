1)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(4))  # False
print(is_prime(7))  # True

2)
def digit_sum(k):
    return sum(map(int, str(k)))
print(digit_sum(24))   # 6
print(digit_sum(502))  # 7

3)
def power_of_two(N):
    result = []
    power = 1
    while power <= N:
        result.append(str(power))
        power *= 2
     print(" ".join(result))
power_of_two(10)
