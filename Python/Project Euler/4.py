def check_pal(x):
    x = str(x)
    return x == x[::-1]


max = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        x = str(i*j)
        if x == x[::-1] and int(x) > max:
            max = int(x)
            index_i = i

print(max, index_i, max/index_i)
