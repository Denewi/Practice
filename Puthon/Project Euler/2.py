def say_sum(n=4000000, ost=0):
    a = 0
    b = 1
    i = 0
    sum = 0

    while i <= n:
        if i % 2 == ost:
            sum += i
        i = a + b
        a = b
        b = i

    print(sum)


say_sum()
