def reverse(self, x: int) -> int:
    """
    Given a 32-bit signed integer, reverse digits of an integer.
    Note:
    Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
    For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
    Input: x = 123
    Output: 321
    """
    res = 0
    
    if x == 0:
        return 0
    
    remains = abs(x)
    sign = -1 if x < 0 else 1

    while True:
        digit = remains % 10
        res = (res * 10) + digit
        remains = remains // 10
        if remains == 0:
            break
    
    res *= sign
    #Check if reversed integer overflows
    if abs(res) > 0x7FFFFFFF:
        return 0
    else:
        return res

