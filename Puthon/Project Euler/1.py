def say_sum(n=10, a=3, b=5):
    i = 0
    sum = 0
    while i != n:
        if (i % a == 0) or (i % b == 0):
            sum += i
        i += 1
    return print(sum)


say_sum()
