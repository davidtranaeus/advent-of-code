import numpy as np
import re

def find_guard(file_name):
  events = []
  with open(file_name, 'r') as f:

    for i in f.readlines():
      date = ''.join(re.findall('[0-9]', i[6:17]))
      events.append([
        date,
        i[19:].strip()
      ])
  
  events.sort(key=lambda e: e[0])
  guard_ids = dict()

  next_id = 0
  for i in events:
    try:
      g_id = int(''.join(re.findall('[0-9]', i[1])))
      if g_id not in guard_ids:
        guard_ids[g_id] = next_id
        next_id += 1
    except:
      continue

  sleep_times = np.zeros((len(guard_ids), 60))

  start = 0 
  for i in events:
    if i[1][0] == 'G':
      current_id = int(''.join(re.findall('[0-9]', i[1])))
    elif i[1][0] == 'f':
      start = int(i[0][-2:])
    else:
      end = int(i[0][-2:])
      sleep_times[guard_ids[current_id]][start:end] += 1
  

  # Part 1
  longest_sleeper_idx = sleep_times.sum(axis=1).argmax()
  sleeper = 0
  for key, value in guard_ids.items():
    if value == longest_sleeper_idx:
      sleeper = key

  minute = np.argmax(sleep_times[longest_sleeper_idx])

  print(sleeper*minute)
  
  # Part 2
  max_min = np.argmax(sleep_times)
  most_frequent_gard_idx = max_min // 60
  most_freq_min = max_min % 60

  freq_sleeper = 0
  for key, value in guard_ids.items():
    if value == most_frequent_gard_idx:
      freq_sleeper = key

  print(freq_sleeper*most_freq_min)



if __name__ == "__main__":
  find_guard('input.txt')
  