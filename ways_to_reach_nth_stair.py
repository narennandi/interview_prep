# A program to count the number of ways to reach n'th stair 

def countWays(n):
    master = []

    for i in range(n+1):

        if i == 0 or i == 1:

            master.append(1)

        else:

            master.append(master[i-1] + master[i-2])

    return master[n]

s = 2
print(countWays(s))
