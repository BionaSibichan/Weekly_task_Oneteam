
import copy

try:
    n = int(input("Enter number of students: "))

    if n <= 0:
        raise ValueError("Number of students must be greater than 0")

    names = []
    roll_numbers = []
    marks = []

    for i in range(n):
        print("\nEnter details of Student", i + 1)

        name = input("Enter name: ")
        roll = int(input("Enter roll number: "))

        mark1 = int(input("Enter mark 1: "))
        mark2 = int(input("Enter mark 2: "))
        mark3 = int(input("Enter mark 3: "))

        if mark1 < 0 or mark1 > 100 or mark2 < 0 or mark2 > 100 or mark3 < 0 or mark3 > 100:
            raise ValueError("Marks must be between 0 and 100")

        names.append(name)
        roll_numbers.append(roll)
        marks.append([mark1, mark2, mark3])

    print("\nStudent Dictionary:")
    student_dict = dict(zip(roll_numbers, names))
    print(student_dict)

    uppercase_names = [name.upper() for name in names]
    print("\nNames in uppercase:")
    print(uppercase_names)

    long_names = [name for name in names if len(name) > 5]
    print("\n Names longer than 5 characters:")
    print(long_names)

    a_count = sum(1 for name in names if name.upper().startswith("A"))
    print("\nNames starting with A:", a_count)

    averages = [sum(m) / 3 for m in marks]

    students_above_75 = [
        names[i] for i in range(n) if averages[i] > 75
    ]

    print("\nStudents with average above 75:")
    print(students_above_75)

    even_roll_numbers = [roll for roll in roll_numbers if roll % 2 == 0]

    print("\nEven roll numbers:")
    print(even_roll_numbers)

    first_student_marks = tuple(marks[0])

    print("\nFirst student's marks as tuple:")
    print(first_student_marks)

    unique_marks = set()

    for m in marks:
        unique_marks.update(m)

    print("\nUnique marks:")
    print(unique_marks)

    shallow_copy = copy.copy(marks)
    deep_copy = copy.deepcopy(marks)

    marks[0][0] = 100

    print("\nOriginal marks:")
    print(marks)

    print("\nShallow copy:")
    print(shallow_copy)

    print("\nDeep copy:")
    print(deep_copy)

except ValueError as e:
    print("\nInvalid input:", e)

except Exception as e:
    print("\nUnexpected error:", e)
