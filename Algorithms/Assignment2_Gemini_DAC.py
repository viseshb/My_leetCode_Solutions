



# #Divide and conquer approach using Gemini 2.0 Flash model
# import math
# import time
# def find_max_crossing_subarray(A, low, mid, high):
#     left_sum = -math.inf
#     sum_val = 0
#     max_left = mid
#     for i in range(mid, low - 1, -1):
#         sum_val += A[i]
#         if sum_val > left_sum:
#             left_sum = sum_val
#             max_left = i

#     right_sum = -math.inf
#     sum_val = 0
#     max_right = mid + 1
#     for j in range(mid + 1, high + 1):
#         sum_val += A[j]
#         if sum_val > right_sum:
#             right_sum = sum_val
#             max_right = j

#     return (max_left, max_right, left_sum + right_sum)

# def find_maximum_subarray(A, low, high):
#     if high == low:
#         return (low, high, A[low])
#     else:
#         mid = (low + high) // 2
#         left_low, left_high, left_sum = find_maximum_subarray(A, low, mid)
#         right_low, right_high, right_sum = find_maximum_subarray(A, mid + 1, high)
#         cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)

#         if left_sum >= right_sum and left_sum >= cross_sum:
#             return (left_low, left_high, left_sum)
#         elif right_sum >= left_sum and right_sum >= cross_sum:
#             return (right_low, right_high, right_sum)
#         else:
#             return (cross_low, cross_high, cross_sum)

# # Example Usage

# A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
# low = 0
# high = len(A) - 1
# start_time = time.perf_counter()
# result = find_maximum_subarray(A, low, high)
# end_time = time.perf_counter()
# print(f"Maximum subarray: {A[result[0]:result[1]+1]}")
# print(f"Sum: {result[2]}")
# print("Execution time (Divide and Conquer using Gemini 2.0):", end_time - start_time, "seconds")
import math
import random
import time

def find_max_crossing_subarray(A, low, mid, high):
    left_sum = -math.inf
    sum_val = 0
    max_left = mid
    for i in range(mid, low - 1, -1):
        sum_val += A[i]
        if sum_val > left_sum:
            left_sum = sum_val
            max_left = i

    right_sum = -math.inf
    sum_val = 0
    max_right = mid + 1
    for j in range(mid + 1, high + 1):
        sum_val += A[j]
        if sum_val > right_sum:
            right_sum = sum_val
            max_right = j

    return (max_left, max_right, left_sum + right_sum)

def find_maximum_subarray(A, low, high):
    if high == low:
        return (low, high, A[low])
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = find_maximum_subarray(A, low, mid)
        right_low, right_high, right_sum = find_maximum_subarray(A, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)

# Generate 100 random prices and calculate daily changes
prices = [random.uniform(50, 150) for _ in range(100)]
daily_changes = [prices[i+1] - prices[i] for i in range(len(prices) - 1)]

# Run Divide-and-Conquer and time it
start_time = time.perf_counter()
result = find_maximum_subarray(daily_changes, 0, len(daily_changes) - 1)
end_time = time.perf_counter()

# Print the table and results
print("Divide-and-Conquer Approach Results:")
print("Day\tPrice\tPrice Change")
for i in range(len(prices)):
    if i == 0:
        print(f"{i + 1}\t{prices[i]:.2f}\tN/A")
    elif i < len(daily_changes) + 1:
        print(f"{i + 1}\t{prices[i]:.2f}\t{daily_changes[i - 1]:.2f}")
    else:
        print(f"{i + 1}\t{prices[i]:.2f}\tN/A")

print(f"\nBest to Purchase on day: {result[0] + 1}")
print(f"Profitable to Trade on day: {result[1] + 2}")  # Corrected: Added 2 instead of 1
print(f"Profit Making: {result[2]:.2f}")
print(f"Execution time (Divide and Conquer using Gemini 2.0 Flash) : {end_time - start_time:.8f} seconds")

import random
import time

def max_subarray_kadane(arr):
    max_ending_here = max_so_far = arr[0]
    start = end = s = 0

    for i in range(1, len(arr)):
        if arr[i] > max_ending_here + arr[i]:
            max_ending_here = arr[i]
            s = i
        else:
            max_ending_here += arr[i]

        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start = s
            end = i

    return start, end, max_so_far

# Generate 100 days of stock prices between $50 and $150
prices = [random.uniform(50, 150) for _ in range(100)]

# Calculating daily changes in prices
daily_changes = [prices[i] - prices[i - 1] for i in range(1, len(prices))]

# Measure execution time
start_time = time.perf_counter()
buy_day, sell_day, max_profit = max_subarray_kadane(daily_changes)
end_time = time.perf_counter()
execution_time_kadane = end_time - start_time

# Display results
print(f"Best to Purchase on day: {buy_day + 1}")
print(f"Profitable to Trade on day: {sell_day + 2}")
print(f"Profit Making: {max_profit:.2f}")
print(f"Execution time (Optimized): {execution_time_kadane:.12f} seconds")
