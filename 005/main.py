import math
import time

# Timer start
start_time = time.perf_counter()

# Code goes here
# Explanation:
# Find the Least Common Multiplier (lcm):
# 1. Decompose all numbers from x to y in prime factors
# 2. Multiply the prime factors that have the highest powers
# e.g. for 20, 19 and 18 this means 20 = 5 * 2², 19 = 19,
#       18 = 2 * 3²; so lcm(20, 19, 18) = 5 * 2² * 3²

print(math.lcm(*[i for i in range(10, 21)]))

# Timer finish
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"The execution time is: {execution_time} seconds")