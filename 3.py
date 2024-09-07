# A prime factor can never be more than half of the numbers own value, unless it is a prime factor itself
# If the number is an uneven nubmber the lowest porential prime factor will be 3, meaning that only a third of the number needs to be checked

def prime(num):
    is_even = num % 2 == 0
    #print(is_even)
    
    l_prime = num
    current = 3
    if is_even:
        num = num / 2
        current = 3
    while current <= num:
        if num % current == 0:
            l_prime = current
            num = num / current

        current += 1
        
        
    print(l_prime)

prime(600851475143)
        