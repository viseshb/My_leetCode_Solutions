# # Divide and conquer approach from Chatgpt 4 legacy model
# import time
# def find_max_crossing_subarray(arr, low, mid, high):
#     left_sum = float('-inf')
#     sum = 0
#     max_left = mid
#     for i in range(mid, low-1, -1):
#         sum += arr[i]
#         if sum > left_sum:
#             left_sum = sum
#             max_left = i
    
#     right_sum = float('-inf')
#     sum = 0
#     max_right = mid
#     for j in range(mid+1, high+1):
#         sum += arr[j]
#         if sum > right_sum:
#             right_sum = sum
#             max_right = j
    
#     return max_left, max_right, left_sum + right_sum

# def find_maximum_subarray(arr, low, high):
#     if high == low:
#         return low, high, arr[low]
#     else:
#         mid = (low + high) // 2
#         left_low, left_high, left_sum = find_maximum_subarray(arr, low, mid)
#         right_low, right_high, right_sum = find_maximum_subarray(arr, mid+1, high)
#         cross_low, cross_high, cross_sum = find_max_crossing_subarray(arr, low, mid, high)
        
#         if left_sum >= right_sum and left_sum >= cross_sum:
#             return left_low, left_high, left_sum
#         elif right_sum >= left_sum and right_sum >= cross_sum:
#             return right_low, right_high, right_sum
#         else:
#             return cross_low, cross_high, cross_sum
# # Example usage
# start_time = time.perf_counter()
# arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
# end_time = time.perf_counter()
# start, end, maximum_sum = find_maximum_subarray(arr, 0, len(arr) - 1)
# print("Maximum subarray:", arr[start:end+1], "with sum:", maximum_sum)
# print("Execution time (Divide and Conquer ChatGPT 4 legacy model):", end_time - start_time, "seconds")
# import random
# import time

# # Function to find the maximum crossing subarray
# def find_max_crossing_subarray(arr, low, mid, high):
#     left_sum = float('-inf')
#     sum_left = 0
#     max_left = mid
#     for i in range(mid, low - 1, -1):
#         sum_left += arr[i]
#         if sum_left > left_sum:
#             left_sum = sum_left
#             max_left = i
    
#     right_sum = float('-inf')
#     sum_right = 0
#     max_right = mid + 1
#     for j in range(mid + 1, high + 1):
#         sum_right += arr[j]
#         if sum_right > right_sum:
#             right_sum = sum_right
#             max_right = j

#     return max_left, max_right, left_sum + right_sum

# # Function to find the maximum subarray using Divide and Conquer
# def find_maximum_subarray_divide_and_conquer(arr, low, high):
#     if high == low:
#         return low, high, arr[low]
#     else:
#         mid = (low + high) // 2
#         left_low, left_high, left_sum = find_maximum_subarray_divide_and_conquer(arr, low, mid)
#         right_low, right_high, right_sum = find_maximum_subarray_divide_and_conquer(arr, mid + 1, high)
#         cross_low, cross_high, cross_sum = find_max_crossing_subarray(arr, low, mid, high)
        
#         if left_sum >= right_sum and left_sum >= cross_sum:
#             return left_low, left_high, left_sum
#         elif right_sum >= left_sum and right_sum >= cross_sum:
#             return right_low, right_high, right_sum
#         else:
#             return cross_low, cross_high, cross_sum

# # Generate 100 days of stock prices between $50 and $150

# prices = [random.randint(50, 150) for _ in range(100)]
# daily_changes = [prices[i] - prices[i-1] for i in range(1, len(prices))]

# # Measure execution time
# start_time = time.perf_counter()
# buy_day, sell_day, max_profit = find_maximum_subarray_divide_and_conquer(daily_changes, 0, len(daily_changes) - 1)
# end_time = time.perf_counter()
# execution_time_dac = end_time - start_time

# # Print stock prices and daily changes
# print("Day | Price  | Change")
# for i in range(len(prices)):
#     if i == 0:
#         print(f"{i+1:<4} {prices[i]:<7} -")
#     else:
#         print(f"{i+1:<4} {prices[i]:<7} {daily_changes[i-1]:.2f}")

# # Display results
# print(f"\nBest to Purchase on day: {buy_day+1}")
# print(f"Profitable to Trade on day: {sell_day+2}")
# print(f"Profit Making: {max_profit:.2f}")
# print(f"Execution time (Divide and Conquer using ChatGPT 4.0 Legacy): {execution_time_dac:.12f} seconds")
import random
import time

# Function to find the maximum crossing subarray
def find_max_crossing_subarray(arr, low, mid, high):
    left_sum = float('-inf')
    sum_left = 0
    max_left = mid
    for i in range(mid, low - 1, -1):
        sum_left += arr[i]
        if sum_left > left_sum:
            left_sum = sum_left
            max_left = i
    
    right_sum = float('-inf')
    sum_right = 0
    max_right = mid + 1
    for j in range(mid + 1, high + 1):
        sum_right += arr[j]
        if sum_right > right_sum:
            right_sum = sum_right
            max_right = j

    return max_left, max_right, left_sum + right_sum

# Function to find the maximum subarray using Divide and Conquer
def find_maximum_subarray_divide_and_conquer(arr, low, high):
    if high == low:
        return low, high, arr[low]  # Handle base case directly
    mid = (low + high) // 2
    left_low, left_high, left_sum = find_maximum_subarray_divide_and_conquer(arr, low, mid)
    right_low, right_high, right_sum = find_maximum_subarray_divide_and_conquer(arr, mid + 1, high)
    cross_low, cross_high, cross_sum = find_max_crossing_subarray(arr, low, mid, high)
    
    # Simplified if-else structure to reduce the number of comparisons
    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= cross_sum:
        return right_low, right_high, right_sum
    return cross_low, cross_high, cross_sum

# Generate 100 days of stock prices between $50 and $150
prices = [random.randint(50, 150) for _ in range(100)]
daily_changes = [prices[i] - prices[i-1] for i in range(1, len(prices))]

# Measure execution time
start_time = time.perf_counter()
buy_day, sell_day, max_profit = find_maximum_subarray_divide_and_conquer(daily_changes, 0, len(daily_changes) - 1)
end_time = time.perf_counter()
execution_time_dac = end_time - start_time

# Display results
print(f"Best to Purchase on day: {buy_day+1}")
print(f"Profitable to Trade on day: {sell_day+2}")
print(f"Profit Making: {max_profit:.2f}")
print(f"Execution time (Divide and Conquer): {execution_time_dac:.12f} seconds")
