import numpy as np

def overlapping(file):
  coords = []
  sizes = []

  with open(file, 'r') as f:
    for i in f.readlines():
      line = i.split()
      coords.append([int(c) for c in line[2][:-1].split(',')])
      sizes.append([int(s) for s in line[3].split('x')])
  
  fabric = np.zeros((1000,1000))

  for i in range(len(coords)):
    x_start = coords[i][0]
    x_end = x_start + sizes[i][0]
    y_start = coords[i][1]
    y_end = y_start + sizes[i][1]

    for y in range(y_start, y_end):
      for x in range(x_start, x_end):
        fabric[y,x] += 1
  
  return len(np.where(fabric > 1)[0])

def unique_claim(file):
  fs = []

  with open(file, 'r') as f:
    for i in f.readlines():
      line = i.split()
      f_id = line[0][1:]
      coord = [int(c) for c in line[2][:-1].split(',')]
      size = [int(s) for s in line[3].split('x')]
      fs.append([
        f_id, 
        coord[0], 
        coord[0] + size[0],
        coord[1],
        coord[1] + size[1]])
  
  for i in range(len(fs)):
    i_x_range = set(range(fs[i][1], fs[i][2]+1))
    i_y_range = set(range(fs[i][3], fs[i][4]+1))
    overlaps = False

    for j in range(len(fs)):
      if i == j:
        continue

      j_x_range = range(fs[j][1],fs[j][2]+1)
      j_y_range = range(fs[j][3],fs[j][4]+1)

      if len(i_x_range.intersection(j_x_range)) > 0 and len(i_y_range.intersection(j_y_range)) > 0:
        overlaps = True
        break
    
    
    if overlaps == False:
      return fs[i][0]
      


if __name__ == "__main__":
  print(overlapping('input.txt'))
  print(unique_claim('input.txt'))