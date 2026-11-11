def first_n_fibonacci(n):
    fibbs = []

    a, b = 0, 1
    for _ in range(n):
        fibbs.append(a)
        a, b = b, a+b
    return fibbs