def add(*numbers):
    return sum(numbers)

def subtract(*numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply(*numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(*numbers):
    if 0 in numbers[1:]:
        return "Cannot divide by zero"
    result = numbers[0]
    for num in numbers[1:]:
        result /= num
    return result

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice (1/2/3/4): ")

num_count = int(input("Enter the number of numbers: "))
numbers = []
for i in range(num_count):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)

if choice == '1':
    result = add(*numbers)
    operator = "+"
elif choice == '2':
    result = subtract(*numbers)
    operator = "-"
elif choice == '3':
    result = multiply(*numbers)
    operator = "*"
elif choice == '4':
    result = divide(*numbers)
    operator = "/"
else:
    print("Invalid input")
    exit()

print(f"Result of {operator.join(map(str, numbers))} = {result}")
