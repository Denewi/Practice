n = 10001

k = 0
t = 2
while 1:
    if all([t % i for i in range(2, 1 + int(t ** 0.5))]):
        k += 1
        if k == n:
            print(t)
            break
    t += 1
