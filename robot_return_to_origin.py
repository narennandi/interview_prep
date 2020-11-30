def judgeCircle(moves):
    x = y = 0

    for move in moves:
        if move == 'U': y -= 1
        if move == 'D': y += 1
        if move == 'R': x -= 1
        if move == 'L': x += 1

    if x == y == 0:
        return True
    else:
        return False

moves = "RL"
print(judgeCircle(moves))