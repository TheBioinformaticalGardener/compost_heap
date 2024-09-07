def fibonacci(max_val):
    past = 1
    now = 2
    sum_total = now
    while  (sum := past + now)  < max_val: 
        past = now
        now = sum 
        #print(now)
        if now % 2 == 0: 
            sum_total += now

    return sum_total
print(fibonacci(4_000_000+1)) # 4613732

