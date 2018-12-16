increment_by_i = [lambda x: x + i for i in range(10)]

for j in range(10):
    print(increment_by_i[j](4))
