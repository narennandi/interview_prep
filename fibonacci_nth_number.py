# Recurssive program to find n'th fibonacci number 
# With memoization
# we are passing a dictionary along with the nth number 

def fibonacci(n, dict_):
    if n == 0:
        return 0
    elif n == 1 or n == 2 :
        return 1
    else:
        if n in dict_:
            return dict_[n]

    result = fibonacci(n-1, dict_) + fibonacci(n-2, dict_)
    dict_[n] = result
    return result

if __name__ == '__main__':
    n = 5
    dict_ = {}
    number = fibonacci(n , dict_)
    print(number)