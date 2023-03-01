generations = 5


def count_neighbours(r, c, alive_nodes):
  count = 0
  # for alive node of the current set and counts them
  for i in range(-1, 2):
    for j in range(-1, 2):
      if (i or j) and (r + i, c + j) in alive_nodes:
        count += 1
  return count


def run_life(alive_nodes):
  # we check the number of generation that is going to be
  for gen in range(generations):
    # create a empty set of the next nodes that is alive
    # set is simlary to a dicnoary, with just keys and no values
    # use for speed of acess, list for fast searching
    next_gen_alive_nodes = set()
    # same for visted notes
    # created for not overlapping neighbors
    visited_nodes = set()
    # iderate the alive nodes
    for i, j in alive_nodes:
      # go through all the neighboards of the current alive node
      # caluclating the delat positions of the
      # start at the top left being -1, -1
      # treverse row wise left to right and top to bottom
      # caluclate the can change nodes
      for di in range(-1, 2):
        for dj in range(-1, 2):
          # to check if current node has been visted already or not
          if (i + di, j + dj) not in visited_nodes:
            # it is not been visted then mark as visted
            visited_nodes.add((i + di, j + dj))
            # calculate alive heighbords for the current node
            neighbours = count_neighbours(i + di, j + dj, alive_nodes)
            # we will be alive in 2 cases:
            # 1. we are currently alive and we have 2 live neighbours (live + neighbours = 2)
            # 2. we have 3 live neighbours (live + neighbours = 3 or dead + neighbour = 3)
            if ((i + di,j + dj) in alive_nodes and neighbours == 2) or neighbours == 3:
              next_gen_alive_nodes.add((i + di, j + dj))
    print(f"gen = {gen}, {next_gen_alive_nodes}")
    alive_nodes = next_gen_alive_nodes


def run():
  #alive_nodes = {(10000000000, 1), (10000000000, 2), (10000000000, 3)}
  alive_nodes = {(0, 1), (1, 2), (2, 0), (2, 1), (2, 2), (-2000000000000, -2000000000000), (-2000000000001, -2000000000001), (-2000000000000, -2000000000001)}
  run_life(alive_nodes)

run()
