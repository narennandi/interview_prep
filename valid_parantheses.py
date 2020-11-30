def isValid(s):
    
    brackets_map = {'(':')', '{': '}', '[' : ']'}
    array = []
    
    for bracket in s:
        
        if bracket in brackets_map:
            array.append(brackets_map[bracket])
        
        elif bracket not in array or bracket != array.pop():
            return False
        
    if not array:
        return True

s =  "()[]{}}"
print(isValid(s))