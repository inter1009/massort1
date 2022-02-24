import random
max_size = 1000  # максимальный размер массива. Изменяется по усмотрению
n = int(input())
a = []
size = []
for i in range(max_size):
    size.append(i + 1)
for i in range(n):
    val = random.randint(0, len(size))
    val1 = size[val - 1]
    del size[val - 1]
    tmp = []
    for j in range(val1):
        x = random.randint(0, 10000000)
        tmp.append(x)
    a.append(tmp)
for i in range(0, n):
    if i % 2 == 0:
        a[i] = sorted(a[i])
    if i % 2 == 1:
        a[i] = sorted(a[i], reverse=True)
print(a)