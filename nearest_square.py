import math
# Importing math for mathematical functions

def nearest_square(n):
    '''nearest_square

    Parameters:
    n (int): To get the nearest square below n

    Returns:
    int 0 : if n is less than 0
    int i : nearest square number but less than n

    '''
    if n<0:
        return 0
    else:
        
        # To find the square of the given number n
        root = math.sqrt(n)
        for i in range(n,-1,-1):
            if int(root)**2 ==i:
                return i
            else:
                continue
        
