import collections
#Breath first search solution

def floodFill(image, sr, sc, newColor):
    old, m, n = image[sr][sc], len(image), len(image[0])
    if old != newColor: 
        q = collections.deque([(sr, sc)])
        while q:
            i, j = q.popleft()
            image[i][j] = newColor
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and image[x][y] == old: 
                    q.append((x, y))
    return image

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1 
sc = 1 
newColor = 2

print(floodFill(image, sr, sc, newColor))