def coinChange(coins, amount):
    inf = float('inf')
    dp = [0] + [inf] * amount

    for i in range(1, amount + 1):
        array = []
        for c in coins:
            if i-c >= 0:
                array.append(dp[i-c])
            else:
                array.append(inf)
        print(min(array))
        dp[i] = min(array) + 1

    return [dp[amount], -1][dp[amount] == inf]

coins = [7,6,5]
amount = 3
print(coinChange(coins, amount))