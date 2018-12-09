import numpy as np

def taxi_dist(x, y):
  return sum(abs(x-y))

def find_area(file_name):

  coords = []
  x_max = 0
  y_max = 0

  with open(file_name, 'r') as f:
    for i in f.readlines():
      line = np.array([int(c.strip()) for c in i.strip().split(',')])
      x_max = line[0] if line[0] > x_max else x_max
      y_max = line[1] if line[1] > y_max else y_max
      coords.append(line)

  field = np.zeros((y_max+1, x_max+1))
  
  even = max([y_max,x_max])*3
  
  for y in range(y_max+1):
    print(y)
    for x in range(x_max+1):

      shortest = even
      for i,c in enumerate(coords):
        
        dist = taxi_dist(c, np.array([x,y]))
        if dist < shortest:
          field[y,x] = i
          shortest = dist
        elif dist == shortest:
          field[y,x] = even

  borders = np.array([np.unique(field[:,0]), np.unique(field[0,:]), np.unique(field[field.shape[0]-1,:]), np.unique(field[:, field.shape[1]-1])])

  border_values = []
  for i in borders:
    for j in i:
      border_values.append(j)

  border_values = np.unique(border_values)

  areas = np.zeros(len(coords))
  for i in range(y_max+1):
    for j in range(x_max+1):
      if field[i,j] == even or field[i,j] in border_values:
        continue
      areas[int(field[i,j])] += 1

  print(int(max(areas)))


def find_region_area(file_name, size):
  coords = []
  x_max = 0
  y_max = 0

  with open(file_name, 'r') as f:
    for i in f.readlines():
      line = np.array([int(c.strip()) for c in i.strip().split(',')])
      x_max = line[0] if line[0] > x_max else x_max
      y_max = line[1] if line[1] > y_max else y_max
      coords.append(line)

  field = np.zeros((y_max+1, x_max+1))

  for y in range(y_max+1):
    print(y)
    for x in range(x_max+1):
      
      dist = 0
      for i,c in enumerate(coords):
        dist += taxi_dist(c, np.array([x,y]))

      if dist < size:
        field[y,x] = 1
  
  print(np.count_nonzero(field))

  

if __name__ == "__main__":
  # find_area('input.txt')
  find_region_area('input.txt', size=10000)

