from math import sqrt
# All primes are odd (except 2 of course)

# We start with 1 999 999 and then go down by 2

# We can start from 3 and then check if the current number 
# is divisible by any of the previous primes


last_digit_check = [1, 3, 7, 9]
current = 5
primes = [3, 5]
stop = 0
while current < 2_000_000:
    print(current)
    if not int(str(current)[-1]) in last_digit_check:
        current += 2
        continue
    else:
        stop = sqrt(current)
        i = 0
        while primes[i] < stop:
        # for i in primes:
            if current % primes[i] == 0:
                break

            i += 1
        else:
            primes.append(current)

        current += 2

# Add the missing prime:
primes = [2]+primes

# print(primes)
print(sum(primes))

142913828922