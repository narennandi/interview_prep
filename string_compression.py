def compress(chars):
    write, count = 0, 0
    
    for i in range(len(chars)):
        count += 1
        
        if i == len(chars) - 1 or chars[i] != chars[i + 1]:
            chars[write] = chars[i]
            write += 1
            
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1        
            count = 0
            
    return write

chars = ["j","a","a","b","b","c","c","c"]
print(compress(chars))
