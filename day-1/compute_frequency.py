import sys

def compute_sum(file_name):
	with open(file_name, 'r') as f:
		final = 0
		lines = f.readlines()
		for l in lines:
			sign = l[0]
			final += int(l[1:]) if l[0] == '+' else -int(l[1:])
	return final

def repeated_freq(file_name):
	with open(file_name, 'r') as f:
		vals = []
		lines = f.readlines()

		for l in lines:
			sign = l[0]
			vals.append(int(l[1:]) if l[0] == '+' else -int(l[1:]))
		
		total = 0
		i = 0
		taken = dict()
		while True:
			total += vals[i % len(vals)]
			if total in taken:
				return total
			else:
				taken[total] = True
				i += 1

	return total

if __name__ == "__main__":
	print('input.txt')
	print('input.txt')