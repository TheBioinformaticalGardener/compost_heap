print(
    sum(
        range(1, 100+1)
    )**2
    -
    sum(
        [x**2 for x in range(1, 100+1)]
    )
)

# 25164150