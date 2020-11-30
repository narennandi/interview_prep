def minHour(rows, columns, grid):
    if not rows or not columns:
        return 0
    
    #find the location of all 1's in grid and store in q
    q = [[i,j] for i in range(rows) for j in range(columns) if grid[i][j]==1]
    # storing direction coordinates
    directions = [[1,0],[-1,0],[0,1],[0,-1]]
    time = 0
    

    while True:
        new = []
        #loop through all the locations of 1's in q
        for [i,j] in q:
            #loop through directions and add the coordinates to current i,j so it
            #moves up, down, left and right
            for d in directions:
                ni, nj = i + d[0], j + d[1]
                #check if location is between zero and number of rows and columns
                #also check if the element == 0, if it is 0 make it 1
                if 0 <= ni < rows and 0 <= nj < columns and grid[ni][nj] == 0:
                    grid[ni][nj] = 1
                    new.append([ni,nj])
        #if nothing is in q break the for loop, else increment time by 1 and start again
        q = new
        if not q:
            break
        time += 1
        
    return time

rows = 4
columns = 5
grid = [[0,1,1,0,1],
        [0,1,0,1,0],
        [0,0,0,0,1],
        [0,1,0,0,0]]

print(minHour(rows, columns, grid))