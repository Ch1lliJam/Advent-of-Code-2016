with open('day1.txt', 'r') as file:
    instructions = file.read().strip().split(', ')

x, y = 0, 0  
direction = 0  # 0 = north, 1 = east, 2 = south, 3 = west
visited = [(x, y)]  # store le co-ordinates

deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]  


for instruct in instructions:
    turn = instruct[0] 
    steps = int(instruct[1:])  

    if turn == 'R':
        direction = (direction + 1) % 4   # %4 if goes over/under 0,1,2,3
    elif turn == 'L':
        direction = (direction - 1) % 4

    for _ in range(steps):
        dx, dy = deltas[direction]
        x += dx
        y += dy

        if (x, y) in visited:
            print(visited)
            print(f"First revisited location: {x}, {y}")
            print(f"Distance to the first revisited location: {abs(x) + abs(y)}")
            exit()  
        
        visited.append((x, y))  


print("fuck")
