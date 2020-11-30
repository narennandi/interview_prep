def firstUniqChar(self, s: str) -> int:
    count = {}
    
    for letter in s:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    
    for letter in count:
        if count[letter] == 1:
            return s.index(letter)
    
    return -1