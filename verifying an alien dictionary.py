def isAlienSorted(words, order):
    
    #create a dict where the key is the letter, value is index of the letter
    order_map = {c:i for i, c in enumerate(order)}
    
    #loop through the words
    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i+1]
        
        #Find the first diff between word1[l] != word2[l]
        for letter in range(min(len(word1), len(word2))):
            if word1[letter] != word2[letter]:
                if order_map[word1[letter]] > order_map[word2[letter]]:
                    return False
                break
            
        else:
            if len(word1) > len(word2):
                return False
            
    return True

if __name__ == '__main__':
    words = ["hello","leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    print(isAlienSorted(words, order))