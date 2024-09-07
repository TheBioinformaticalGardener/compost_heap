# if it is devisible by 20 it must be an even number

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
16    

#check_list = [
#    20, 19, 18, 17, 16, 15, 14, 13, 12, 11
#]
check_list = list(range(1, 11))
def foo(check_list):
    # Make start number even
    current = 2
    if current % 2 != 0:
        current += 1
    running = True
    while running:
        for i in check_list:
            if current % i != 0:
                current += 10
                break
         
        return current
         
print(foo(check_list))
