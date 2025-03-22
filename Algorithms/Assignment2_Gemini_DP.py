
# # Dynamic programming approach from Gemini 2.0 Flash model
# import math
# import time

# def max_subarray_kadane(A):
#     max_at_index = 0
#     max_so_far = -math.inf
#     low = 0
#     high = 0
#     t = 0

#     for i in range(len(A)):
#         max_at_index += A[i]
#         if max_at_index > max_so_far:
#             max_so_far = max_at_index
#             low = t
#             high = i

#         if max_at_index < 0:
#             max_at_index = 0
#             t = i + 1

#     return max_so_far, A[low:high+1]

# # Example Usage

# A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
# start_time = time.perf_counter()  # Start timer *before* the algorithm
# max_sum, subarray = max_subarray_kadane(A)
# end_time = time.perf_counter()    # End timer *after* the algorithm
# print(f"Maximum subarray: {subarray}")
# print(f"Sum: {max_sum}")
# print("Execution time (Dynamic Programming using Gemini 2.0):", end_time - start_time, "seconds")
import math
import random
import time

def max_subarray_kadane(A):
    max_at_index = 0
    max_so_far = -math.inf
    low = 0
    high = 0
    t = 0

    for i in range(len(A)):
        max_at_index += A[i]
        if max_at_index > max_so_far:
            max_so_far = max_at_index
            low = t
            high = i

        if max_at_index < 0:
            max_at_index = 0
            t = i + 1

    return max_so_far, low, high # Return low and high indices instead of subarray

# Generate 100 random prices and calculate daily changes
prices = [random.uniform(50, 150) for _ in range(100)]
daily_changes = [prices[i+1] - prices[i] for i in range(len(prices) - 1)]

# Run Kadane's Algorithm and time it
start_time = time.perf_counter()
max_sum, low, high = max_subarray_kadane(daily_changes) # Get low and high indices
end_time = time.perf_counter()

# Print the table and results
print("Kadane's Algorithm Approach Results:")
print("Day\tPrice\tPrice Change")
for i in range(len(prices)):
    if i == 0:
        print(f"{i + 1}\t{prices[i]:.2f}\tN/A")
    elif i < len(daily_changes) + 1:
        print(f"{i + 1}\t{prices[i]:.2f}\t{daily_changes[i - 1]:.2f}")
    else:
        print(f"{i + 1}\t{prices[i]:.2f}\tN/A")

# Corrected Day Calculation
purchase_day = low + 1
trade_day = high + 2

# Ensure trade day is not before purchase day
if trade_day < purchase_day:
    trade_day = purchase_day

print(f"\nBest to Purchase on day: {purchase_day}")
print(f"Profitable to Trade on day: {trade_day}")
print(f"Profit Making: {max_sum:.2f}")
print(f"Execution time (Dynamic Programming using Gemini 2.0 Flash) : 0.00006850 seconds: {end_time - start_time:.6f} seconds")