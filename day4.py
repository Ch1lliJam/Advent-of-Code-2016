import collections
total_sector_id = 0  


with open('day4.txt', 'r') as file:
    day4 = file.readlines()  

for line in day4:
    line = line.strip()  
    
    encrypted_name, sector_id_checksum = line.rsplit('-', 1)
    
    sector_id, checksum = sector_id_checksum.split('[')  
    sector_id = int(sector_id)  
    checksum = checksum.strip(']')  
    
    name = encrypted_name.replace('-', '')
    letter_counts = collections.Counter(name)   # basically lazy way of automatically counting each letter (imported library)
                                                # https://docs.python.org/3/library/collections.html
    
    sorted_letters = sorted(letter_counts.items(), key=lambda x: (-x[1], x[0]))
    most_common_letters = ''.join([letter for letter, count in sorted_letters[:5]])


    if most_common_letters == checksum:
        total_sector_id += sector_id 
    

print(f"Sum of sector IDs of real rooms: {total_sector_id}")