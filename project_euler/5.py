'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible with no remainder by all of the numbers from 1 to 20?
'''
# Thoughts:
# We know that the number must be 2520 or greater.
# If it is divisible by 20 it must be an even number.
# It must also be part of 20*n, meaning that we can add 20 for each try.
# We probably do not need to check if the number is divisible by 10 or less since all numbers up to 20 is divisible by some of those numbers anyway. 

'''
To check:
    1x
    2x
    3x
    4x
    5x
    6
    7
    8x
    9x
    10x
    11
    12
    13
    14
    15x
    16x
    17x
    18x
    19x
    20x
'''   

check_list = [
   20, 19, 18, 17, 16, 15, 14, 13, 12, 11
]
# check_list = list(range(1, 11))
def foo(check_list):
    # Make sure start number is even
    current = 20
    #if current % 2 != 0:
     #   current += 1
    
    running = True
    while running:
        print(current)
        for i in check_list:
            if current % i != 0:
                current += 20
                break
        else:
            running = False
    
    return current

         
print(foo(check_list))
