import math
import time

# Timer start
start_time = time.perf_counter()

# Code goes here
def is_prime(number: int):
  if number == 1:
    return True
  for i in range(2, int(math.sqrt(number))+1):
    if number % i == 0:
      return False
  return True


NUMBER = 600851475143
start = round(math.sqrt(NUMBER))
for i in range(start, 3, -1):
  is_factor = NUMBER % i == 0
  if is_factor and is_prime(i):
    print(f'Success!')
    print(i)
    break


# Timer finish
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"The execution time is: {execution_time} seconds")