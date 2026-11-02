n = 10
a = 0
b = 1
print(f"The first {n} Fibonacci numbers are:")
for _ in range(n):
    print(a)
    next_num = a + b
    a = b
    b = next_num