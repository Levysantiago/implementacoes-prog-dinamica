def fibonacci(n):
    if(n==1):
        return 0
    if(n == 2):
        return 1
    l = [-1, 0, 1]
    for i in range(3, n+1):
        l.append(l[i-1] + l[i-2])
    print(l)
    return l.pop()

print(fibonacci(10))