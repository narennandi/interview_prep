def longestStrChain(words):
    dp = {}
    result = 1

    for word in sorted(words, key=len):
        dp[word] = 1

        for i in range(len(word)):
            prev = word[:i] + word[i + 1:]
            print(prev)
            if prev in dp:
                dp[word] = max(dp[prev] + 1, dp[word])
                result = max(result, dp[word])

    return result


words = ["bdca"]
# words = ["a","b","ba","bca","bda","bdca"]
print(longestStrChain(words))


# sort the list by length of the words
# loop through each set of words and check if it exists in dictionary
# If exists, 