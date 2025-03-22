# # Dynamic programming approach from Chatgpt 4 legacy model
# import time
# def max_subarray_kadane(arr):
#     max_ending_here = max_so_far = arr[0]
#     start = end = s = 0

#     for i in range(1, len(arr)):
#         if arr[i] > max_ending_here + arr[i]:
#             max_ending_here = arr[i]
#             s = i
#         else:
#             max_ending_here += arr[i]

#         if max_ending_here > max_so_far:
#             max_so_far = max_ending_here
#             start = s
#             end = i

#     return arr[start:end+1], max_so_far

# # Example usage
# start_time = time.perf_counter()
# arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
# end_time = time.perf_counter()
# subarray, maximum_sum = max_subarray_kadane(arr)
# print("Maximum subarray:", subarray, "with sum:", maximum_sum)
# print("Execution time (Dynamic Programming using ChatGPT 4 legacy model):", end_time - start_time, "seconds")
import random
import time

# Function to find the maximum subarray sum using Kadane's Algorithm
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
daily_changes = [prices[i] - prices[i-1] for i in range(1, len(prices))]

# Measure execution time
start_time = time.perf_counter()
buy_day, sell_day, max_profit = max_subarray_kadane(daily_changes)
end_time = time.perf_counter()
execution_time_kadane = end_time - start_time

# Print stock prices and daily changes
print("Day | Price  | Change")
for i in range(len(prices)):
    if i == 0:
        print(f"{i+1:<4} {prices[i]:.2f} -")
    else:
        print(f"{i+1:<4} {prices[i]:.2f} {daily_changes[i-1]:.2f}")

# Display results
print(f"\nBest to Purchase on day: {buy_day+1}")
print(f"Profitable to Trade on day: {sell_day+2}")
print(f"Profit Making: {max_profit:.2f}")
print(f"Execution time (Dynamic Programming using ChatGPT 4.0 Legacy Model): {execution_time_kadane:.12f} seconds")
