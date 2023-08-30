def calculate_average(numbers):
    if len(numbers) == 0:
        return None  # Return None for an empty list
    
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Taking user input for the list of numbers
num_str = input("Enter a list of numbers separated by spaces: ")
num_list = [float(num) for num in num_str.split()]

result = calculate_average(num_list)
if result is not None:
    print(f"The average of the numbers is: {result:.2f}")
else:
    print("The list is empty.")

