def check(max):
    i = 2
    while i <= max // 2:
        if max % i == 0:
            return 0
        i += 1
    return 1


def say_div(n=600851475143):
    i = 2
    max = 0

    while i <= n // 2:
        if n % i == 0:
            max = n // i
            if check(max):
                break
        i += 1

    print(max)


say_div()
