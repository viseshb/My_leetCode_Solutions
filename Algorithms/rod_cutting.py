def rod_cutting(prices, n):
    # prices list is 1-indexed; prices[i] gives price of rod of length i
    # r[i] will hold the maximum profit for rod of length i
    r = [0] * (n + 1)

    # Solve for each length 1 to n
    for j in range(1, n + 1):
        # Initialize maximum revenue for length j
        q = -float('inf')
        # Try every cut possible
        for i in range(1, j + 1):
            q = max(q, prices[i] + r[j - i])
        r[j] = q
    return r[n]

# Example prices given (1-indexed, 0th index is dummy to align with natural index)
prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]  # Include a zero at the start to align indices
max_length = 9

# Compute the maximum profit for a rod of length 10
max_profit = rod_cutting(prices, max_length)
print(f"The maximum profit for a rod of length {max_length} is: ${max_profit}")
