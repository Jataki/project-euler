import time

# Timer start
start_time = time.perf_counter()

# Code goes here
singles = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
tenths = [0, 4, 6, 6, 5, 5, 5, 7, 6, 6]
hundreds = 7 # singles[i] + hundreds (e.g. one hundred = 3 + 7)
exceptions = {10: 3, 11: 6, 12: 6, 13: 8, 15: 7, 18: 8}

total = 11 # one thousand = 11 letters
one_to_99 = 0 # count from 1 to 99
for i in range (1, 100):
  if i >= 10:
    one_to_99 += tenths[i // 10] + singles[i % 10] if not exceptions.get(i) else exceptions[i]
  else:
    one_to_99 += singles[i]

total += one_to_99
for i in range(1, 10):
  total += singles[i] + hundreds # 100, 200, 300, ...
  total += (singles[i] + hundreds + 3)*99 + one_to_99 # 101-199, 201-299, ...
print(total)

# Timer finish
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"The execution time is: {execution_time} seconds")