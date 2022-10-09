import time

# Timer start
start_time = time.perf_counter()

# Code goes here
answer = 999999
chains = {}
biggest_chain = 0
for i in range(999999, 500000, -1):
  j = i
  chain = 0
  stack = []
  while j > 2:
    j_chain = chains.get(j)
    if j_chain:
      chain += j_chain
      break
    # continue sequence
    chain += 1
    stack.append(j)
    if j % 2 == 0: j = j // 2
    else: j = 3*j + 1
  # fill the chain values
  for idx, el in enumerate(stack):
    chains[el] = chain - idx
  if chain > biggest_chain:
    answer = i
    biggest_chain = chain
print(answer)

# Timer finish
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"The execution time is: {execution_time} seconds")