import sys

def compute_result(file_name):
	with open(file_name, 'r') as f:
		final = 0
		lines = f.readlines()
		for l in lines:
			sign = l[0]
			final += int(l[1:]) if l[0] == '+' else -int(l[1:])
	return final

if __name__ == "__main__":
	print(compute_result(sys.argv[1]))