def sum_k(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i ** 2
    return sum


def k_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum ** 2


n = 20
print('Разность:', k_sum(n) - sum_k(n))
