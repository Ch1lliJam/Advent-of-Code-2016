counter = 0 
triangle_groups = [[], [], []] 

with open("day3.txt", 'r') as file:
    lines = file.readlines()



for line in lines:
    numbers = list(map(int, line.strip().split()))  # turn into list of integers
    for i in range(3):
        triangle_groups[i].append(numbers[i])  # put number lists into triangle_groups array


for group in triangle_groups:
    for i in range(0, len(group), 3):  
        if i + 2 < len(group):  # check if possible
            num1 = group[i] 
            num2 = group[i+1] 
            num3 = group[i+2]
            largest = max(num1, num2, num3)  # find largest of teh 3
            sum_of_smaller = num1 + num2 + num3 - largest  
            
            if sum_of_smaller > largest:
                counter += 1  


print(f"Final value of the counter: {counter}")