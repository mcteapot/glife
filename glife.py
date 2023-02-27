#glife 
generations = 5


def count_neighbours(r, c, alive_nodes):
  count = 0
  for i in range(-1, 2):
    for j in range(-1, 2):
      if (i or j) and (r + i, c + j) in alive_nodes:
        count += 1
  return count


def run_life(alive_nodes):
  for gen in range(generations):
    next_gen_alive_nodes = set()
    visited_nodes = set()
    for i, j in alive_nodes:
      for di in range(-1, 2):
        for dj in range(-1, 2):
          if (i + di, j + dj) not in visited_nodes:
            visited_nodes.add((i + di, j + dj))
            neighbours = count_neighbours(i + di, j + dj, alive_nodes)
            if ((i + di,j + dj) in alive_nodes and neighbours == 2) or neighbours == 3:
              next_gen_alive_nodes.add((i + di, j + dj))
    print(f"gen = {gen}, {next_gen_alive_nodes}")
    alive_nodes = next_gen_alive_nodes


def run():
  alive_nodes = {(10000000000, 1), (10000000000, 2), (10000000000, 3)}
  run_life(alive_nodes)


run()
