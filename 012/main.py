import math
import time

# Timer start
start_time = time.perf_counter()

# Code goes here
# If N is divisible by X and X <= sqrt(N), then
# there is also a number Y >= sqrt(N) such that X*Y = N
# Thus finding X means finding 2 numbers
def count_divisors(number: int) -> int:
  count = 1
  for i in range(1, round(math.sqrt(number)) + 1):
    if number % i == 0:
      count += 2
  return count

i = 7
triangle = 28
while True:
  i += 1
  triangle += i  
  if count_divisors(triangle) > 500:
    print(triangle)
    break

# Timer finish
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"The execution time is: {execution_time} seconds")