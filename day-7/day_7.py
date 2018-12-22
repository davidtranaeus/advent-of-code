import numpy as np
import string

def find_steps(file_name):

  pairs = []
  with open(file_name, 'r') as f:
    for i in f.readlines():
      pairs.append(np.array([i[36],i[5]]))

  pairs = np.array(pairs)

  idx_to_letter = np.unique(pairs.flatten())
  letter_to_idx = dict()

  for c,i in enumerate(idx_to_letter):
    letter_to_idx[i] = c

  dim = len(letter_to_idx)
  adj = np.zeros((dim, dim))

  for i in pairs:
    adj[letter_to_idx[i[0]],letter_to_idx[i[1]]] = 1

  debug = np.copy(adj)

  taken = np.zeros(dim)
  steps = ''

  while len(steps) != dim:
    print(adj)
    for i in range(len(adj)):
      if taken[i]:
        continue

      if not adj[i].any():
        print(i)
        steps += idx_to_letter[i]
        taken[i] = 1
        adj[:,i] = 0
        break
    # print('--')
  return steps

def total_time(file_name, n_workers):
  pairs = []
  with open(file_name, 'r') as f:
    for i in f.readlines():
      pairs.append(np.array([i[36],i[5]]))

  pairs = np.array(pairs)

  idx_to_letter = np.unique(pairs.flatten())
  letter_to_idx = dict()

  for c,i in enumerate(idx_to_letter):
    letter_to_idx[i] = c

  dim = len(letter_to_idx)
  adj = np.zeros((dim, dim))

  for i in pairs:
    adj[letter_to_idx[i[0]],letter_to_idx[i[1]]] = 1

  taken = np.zeros(dim)
  seconds = -1
  letter_times = np.arange(dim) + 1 + 60

  while letter_times.any():

    for i in np.where(taken == 1)[0]:
      if letter_times[i] != 0:
        letter_times[i] -= 1
  
    for i in range(len(letter_times)):
      if taken[i] and letter_times[i] == 0:
        adj[:,i] = 0

    for i in range(len(adj)):
      if taken[i]:
        continue

      taken_letters = np.where(taken == 1)[0]
      n_still_active = len(np.where(letter_times[taken_letters] > 0)[0])

      if not adj[i].any() and n_still_active < n_workers:
        taken[i] = 1

    seconds += 1
    # print(letter_times, end=' ')
    # for i in np.where(letter_times == 0)[0]:
    #   print(idx_to_letter[i], end='')
    # print()
    
  print(seconds)

          

if __name__ == "__main__":
  # print(find_steps('test.txt'))
  total_time('input.txt', n_workers=5+1)