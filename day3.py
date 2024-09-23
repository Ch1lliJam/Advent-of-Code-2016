counter = 0  # Initialize the counter

with open("day3.txt", "r") as input_file:
    rawinput = input_file.read()
    lines = rawinput.strip().split('\n')  # Read all lines from the file

for line in lines:
    numbers = list(map(int, line.split()))  # Split the line into numbers and convert them to integers
    if len(numbers) == 3:  # Ensure there are exactly 3 numbers
        num1, num2, num3 = numbers  # Assign the numbers
        largest = max(num1, num2, num3)  # Find the largest number
        sum_of_smaller = num1 + num2 + num3 - largest  # Sum of the two smaller numbers
        
        # Check if the sum of the two smaller numbers is greater than the largest number
        if sum_of_smaller > largest:
            counter += 1  # Update the counter if condition is true

# Print the final value of the counter
print(f"Final value of the counter: {counter}")