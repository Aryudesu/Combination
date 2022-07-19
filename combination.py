def inputNum(mes="InputNum > "):
    while True:
        try:
            print(mes, end="")
            return int(input())
        except:
            print('Input "Num" Please')


def combination(a, b):
    n, m = a, b
    if n < 2 * m:
        m = n - m
    if n == m or m == 0:
        return 1
    tmp = [n - i for i in range(m)]
    for i in range(1, m + 1):
        for j in range(m):
            if not tmp[j] % i:
                tmp[j] //= i
                break
    result = 1
    for i in tmp:
        result *= i
    return result


num = inputNum()
for i in range(num + 1):
    tmp = []
    for j in range(i + 1):
        tmp.append(str(combination(i, j)))
    print(" ".join(tmp))
