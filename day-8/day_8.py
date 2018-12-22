import numpy as np

class Node():
  def __init__(self):
    self.children = []
    self.meta = []
    self.value = 0

def create_node(data, idx):
  n_children = data[idx]
  n_meta = data[idx+1]
  node = Node()

  if n_children > 0:
    while len(node.children) < n_children:
      child, data = create_node(data, idx+2)
      node.children.append(child)

  node.meta = data[idx+2:idx+2+n_meta]
  data = np.delete(data, range(idx, idx+2+n_meta))
  return node, data

def build_tree(data):
  return create_node(data, 0)[0]

def get_meta_sum(node):
  total = sum(node.meta)
  for i in node.children:
    total += get_meta_sum(i)
  return total

def get_node_value(node):
  if len(node.children) == 0:
    return sum(node.meta)
  else:
    val = 0
    for i in node.meta:
      if i <= len(node.children):
        val += get_node_value(node.children[i-1])
    return val

def problems():
  file_name = 'input.txt'
  with open(file_name, 'r') as f:
    data = [int(i) for i in f.readline().strip().split(' ')]

  root = build_tree(data)
  print(get_meta_sum(root))
  print(get_node_value(root))


if __name__ == "__main__":
  problems()