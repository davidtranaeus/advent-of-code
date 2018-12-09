import numpy as np
import string

def react_polymer(file_name):
  
  with open(file_name, 'r') as f:
    data = f.readline().strip()

  lengths = []

  for i in string.ascii_lowercase:
    line_data = data
    print('Removing char', i, 'and reacting polymer')
    line_data = ''.join(line_data.split(i)).strip()
    line_data = ''.join(line_data.split(i.upper())).strip()

    res = len(do_reaction(line_data))
    lengths.append(res)
    
  print(min(lengths))
  

def do_reaction(line):
  reacted = True

  while reacted:

    reacted = False
    prev = ''

    for i in range(len(line)):
      if i == len(line)-1:
        break

      if (line[i].isupper() and line[i].lower() == line[i+1]) or (line[i].islower() and line[i].upper() == line[i+1]):

        line = line[:i] + line[i+2:]
        reacted = True
        break
    
  return line

if __name__ == "__main__":
  react_polymer('input.txt')