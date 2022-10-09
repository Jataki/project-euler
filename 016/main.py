import time

# Timer start
start_time = time.perf_counter()

# Code goes here
print(sum(int(i) for i in str(2**1000)))

# Timer finish
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"The execution time is: {execution_time} seconds")