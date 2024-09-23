import collections
total_sector_id = 0  
string = ""
string2 = ""
columns = []

with open('day6.txt', 'r') as file:
    day6 = file.readlines()
    
    for line in day6:
        line = line.strip()

num_columns = len(day6[0])                  # dumb assumption that all rows are same length (they are)
for i in range(num_columns):
    columns.append('') 


for line in day6:
    for i, char in enumerate(line):
        columns[i] += char  


for i in columns:
    letter_counts = collections.Counter(i)
    sorted_letters = sorted(letter_counts.items(), key=lambda x: (-x[1], x[0]))
    most_common_letter = sorted_letters[0][0]
    least_common_letter = sorted_letters[-1][0]
    string += most_common_letter
    string2 += least_common_letter

print(string)
print(string2)