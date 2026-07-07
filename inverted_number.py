def inverted_numbers(rows):
    for i in range(rows, 0, -1):
        line = ""
        for num in range(1, i + 1):
            line += str(num)
        print(line)
inverted_numbers(4)