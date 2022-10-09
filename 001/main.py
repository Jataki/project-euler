import time

# Timer start
start_time = time.perf_counter()

# Code goes here
sum = 0
for i in range(0, 1000):
  if i % 3 == 0 or i % 5 == 0:
    sum += i
print(sum)

# Timer finish
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"The execution time is: {execution_time} seconds")