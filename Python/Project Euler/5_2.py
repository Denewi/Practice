alf_sost = []


def sost(n=100):
    if all([n % i for i in range(2, 1 + int(n ** 0.5))]):
        alf_sost.append(n)
    else:
        for i in range(2, int(n // 2) + 1):
            if n % i == 0:
                alf_sost.append(i)
                sost(n // i)
                break


alf = []
# n = int(input('Введите число: '))
n = 100000
for i in range(2, n + 1):
    sost(i)
    alf_temp = alf.copy()
    for i in alf_sost:
        if i in alf_temp:
            alf_temp.remove(i)
        else:
            alf.append(i)
    alf_sost = []

sum = 1
for i in alf:
    sum *= int(i)

print(sum)
