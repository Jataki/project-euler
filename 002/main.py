import time

# Timer start
start_time = time.perf_counter()

# Code goes here
sum = 2
last_fib = 2
curr_fib = 3
while curr_fib <= 4000000:
  new_fib = curr_fib + last_fib
  last_fib = curr_fib
  curr_fib = new_fib
  if curr_fib % 2 == 0:
    sum += curr_fib
print(sum)


# Timer finish
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"The execution time is: {execution_time} seconds")