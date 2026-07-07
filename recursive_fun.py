def sum_natural_no(n):
    if n <= 0:
        return 0
    else:
        return n + sum_natural_no(n - 1)
print (sum_natural_no(7))