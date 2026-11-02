num = 7777
while num > 9:
    total = 0
    for digit in str(num):
        total += int(digit)
    num = total
print("Single-digit sum:", num)