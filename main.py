# Task 1: Python Data Handling Practical

# ---------- Part 1: Mean, Median, Min, Max ----------

def calculate_statistics(numbers):
    total = 0
    count = len(numbers)

    for num in numbers:
        total += num

    mean = total / count

    sorted_numbers = sorted(numbers)
    mid = count // 2

    if count % 2 == 0:
        median = (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        median = sorted_numbers[mid]

    minimum = sorted_numbers[0]
    maximum = sorted_numbers[-1]

    return mean, median, minimum, maximum


# ---------- Part 2: Top 3 Students ----------

def top_three_students(students):
    sorted_students = sorted(students.items(), key=lambda x: x[1], reverse=True)
    return sorted_students[:3]


# ---------- Part 3: Sum of Numbers from File ----------

def sum_from_file(filename):
    total = 0
    with open(filename, 'r') as file:
        for line in file:
            total += int(line.strip())
    return total


# ---------- Main Program ----------

def main():
    # List of 30 numbers
    numbers = [
        12, 45, 67, 23, 89, 90, 34, 56, 78, 11,
        22, 33, 44, 55, 66, 77, 88, 99, 100, 5,
        15, 25, 35, 46, 57, 68, 79, 81, 92, 10
    ]

    mean, median, minimum, maximum = calculate_statistics(numbers)

    print("Statistics:")
    print("Mean:", mean)
    print("Median:", median)
    print("Minimum:", minimum)
    print("Maximum:", maximum)
    print("-" * 40)

    # Dictionary of students
    students = {
        "Tasmiya": 85,
        "Adeena": 92,
        "Aadil": 78,
        "Hamdan": 88,
        "zaidi": 90,
        "haani": 95,
        "Karan": 80,
        "Anjali": 89,
        "Vikas": 76,
        "Meena": 91
    }

    top_students = top_three_students(students)

    print("Top 3 Scorers:")
    for name, marks in top_students:
        print(name, ":", marks)
    print("-" * 40)

    # File handling
    filename = "numbers.txt"
    total_sum = sum_from_file(filename)

    print("Sum of numbers from file:", total_sum)


if __name__ == "__main__":
    main()
