import time

# Timer start
start_time = time.perf_counter()

# Code goes here
square_sum = 0
sum_square = 0
for i in range(1, 101):
  square_sum += i
  sum_square += i**2
square_sum = square_sum**2
print(abs(sum_square - square_sum))

# Timer finish
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"The execution time is: {execution_time} seconds")