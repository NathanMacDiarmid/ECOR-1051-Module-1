def accumulated_amount(principal, rate, n, time):
    x = 1 + (rate / n)
    y = n * time
    return principal * (x**y)


print(accumulated_amount(1500, 0.043, 4, 6))
print(accumulated_amount(0, 0.043, 4, 6))
print(accumulated_amount(1500, 0, 4, 6))
