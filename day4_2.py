import collections


def caesar_cipher_shift(name, sector_id):
    shifted_name = []
    
    for char in name:
        if char.isalpha():  
            new_char = chr((ord(char) - ord('a') + sector_id) % 26 + ord('a'))
            shifted_name.append(new_char)
        else:
            shifted_name.append(char)
    
    return ''.join(shifted_name)

with open('day4.txt', 'r') as file:
    day4 = file.readlines()  

for line in day4:
    line = line.strip()  
    
    encrypted_name, sector_id_checksum = line.rsplit('-', 1)
    

    sector_id, checksum = sector_id_checksum.split('[')  
    sector_id = int(sector_id) 
    checksum = checksum.strip(']') 
    

    name = encrypted_name.replace('-', ' ')
    
    shifted_name = caesar_cipher_shift(name, sector_id)
    print(f"Shifted name: {shifted_name} (Sector ID: {sector_id})")
    




    
