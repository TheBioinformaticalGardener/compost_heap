import math
from time import sleep

def palindrome(digits):
    left = int("9"*digits)
    right = left
    switch = True
    
    while True:
        #print(left, '\t*\t', right)
        #sleep(2)
        product = str(left * right)
        #print(product)
        if product[0] == product[-1]:
            length = len(product)
            #print(length)
            if length % 2 == 0:
                half = int(length / 2)
                #print(product[:half], ' - ', product[half:])
                if product[:half] == product[half:][::-1]:
                    return product
            else:
                section = math.floor(length)
                if product[:section] == product [section+1:][::-1]:
                    return product
         
        if switch:
             left -= 1
             if left ==0:          
                 switch = False
        else: 
             right -=1
             switch = True
             
print(palindrome(3))
# too slow!