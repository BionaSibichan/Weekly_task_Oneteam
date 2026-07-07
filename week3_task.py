def pyramid(rows):
    for i in range(1, rows + 1):
        spaces = rows - i
        stars = 2 * i - 1
        print(" " * spaces + "*" * stars)

def inverted_numbers(rows):
    for i in range(rows, 0, -1):
        line = ""
        for num in range(1, i + 1):
            line += str(num)
        print(line)

def sum_natural_no(n):
    if n <= 0:
        return 0
    return n + sum_natural_no(n - 1)


power = lambda base, exp: base ** exp

def show_menu():
    print("1. Print Pyramid Star Pattern")
    print("2. Print Inverted Number Pattern")
    print("3. Calculate Sum of First N Natural Numbers")
    print("4. Calculate Power of a Number Lambda")
    print("5. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            
            pyramid(4)

        elif choice == "2":
            
            inverted_numbers(4)

        elif choice == "3":
            n = int(input("Enter the value of N: "))
            print(f"Sum of first {n} natural numbers is: {sum_natural_no(n)}")

        elif choice == "4":
            base = float(input("Enter the base number: "))
            exp = float(input("Enter the exponent: "))
            result = power(base, exp)
            print(f"{base} raised to the power {exp} is: {result}")

        elif choice == "5":
            print("Exit")
            break

        else:
            print("Invalid choice")

main()
