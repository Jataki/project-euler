import time

# Timer start
start_time = time.perf_counter()

# Code goes here
# First solution that came to mind was a recursive counter
# that proved too slow
# GRID_SIZE = 20
# def count_moves(coord: tuple, counter: int):
#   if coord != (GRID_SIZE, GRID_SIZE):
#     if coord[0] != GRID_SIZE:
#       counter = count_moves((coord[0] + 1, coord[1]), counter)
#     if coord[1] != GRID_SIZE:
#       counter = count_moves((coord[0], coord[1] + 1), counter)
#   else:
#     return counter + 1
#   return counter
# print(count_moves((0,0), 0))

# Understood this problem is a mere tree traversing:
# with every node in the x-axis and y-axis being one, each
# other node is but the sum of the previous row and column values
nodes_cardinality = 20 + 1 # number of sides + root
tree = [[0] * nodes_cardinality for _ in range(0, nodes_cardinality)]
for i in range(1, nodes_cardinality):
  tree[0][i] = 1
  tree[i][0] = 1

for i in range(1, nodes_cardinality):
  for j in range(1, nodes_cardinality):
    tree[i][j] = tree[i][j-1] + tree[i-1][j]
print(tree[20][20])

# Timer finish
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"The execution time is: {execution_time} seconds")