import numpy as np

def checksum(file_name):
	with open(file_name, 'r') as f:

		twos = 0
		threes = 0

		for l in f.readlines():
			values, counts = np.unique(list(l.strip()), return_counts=True)
			twos += 1 if 2 in counts else 0
			threes += 1 if 3 in counts else 0
			
	return twos * threes

def common_chars(file_name):
	with open(file_name, 'r') as f:

		strings = [f.readline().strip()]

		for line in f.readlines():
			line = line.strip()

			for s in strings:
				diff = [line[i] for i in range(len(line)) if s[i] == line[i]]

				if len(diff) == len(line)-1:
					return ''.join(diff)

			strings.append(line)
			
	return 0


if __name__ == "__main__":
	print(checksum('input.txt'))
	print(common_chars('input.txt'))