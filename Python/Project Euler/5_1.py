def check_del(n):
    for i in range(2, 15):
        if n % i != 0:
            return 0
    return 1


i = 100
while 1:
    if check_del(i):
        break
    print(i)
    i += 10

print(i)
