#a word, phrase, or sequence that reads the same backward 
# as forward, e.g., madam or nurses run.

def longestPalindrome(s):
    m = ''  # Memory to remember a palindrome
    for i in range(len(s)):  # i = start, O = n
        for j in range(len(s), i, -1):  # j = end, O = n^2
            if len(m) >= j-i:  # To reduce time
                break
            elif s[i:j] == s[i:j][::-1]:
                m = s[i:j]
                break
    return m

s = "babad"
print(longestPalindrome(s))

