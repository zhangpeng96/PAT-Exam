import timeit

def parse(matrix):
	string = ''
	for arr in matrix:
		string += ''.join(map(lambda x: ' {:>2d}'.format(x), arr))
		string += '\n'
	return(string.rstrip())

def row_shift(row_arr, length, fill):
	return [fill] * length + row_arr[0:-length]


def main():
	matrix = []
	matrix_count, shift_k, fill_value = list(map(int, input().split()))
	ins_list = []
	for i in range(0, matrix_count):
		ins_list.append(input())

	ts_start =  timeit.default_timer()

	for ins in ins_list:
		matrix.append(list(map(int, ins.split())))

	shift_count = 0
	shift_k_list = [1, shift_k]

	for r, row in enumerate(matrix):
		if (r + 1) % 2:
			matrix[r] = row_shift(matrix[r], shift_k_list[(shift_count % 2)], fill_value)
			shift_count += 1

	result = [0]*matrix_count
	for row in matrix:
		for i, r in enumerate(row):
			result[i] += r
	print(' '.join(map(str, result)))

	print('{:.3f}ms'.format((timeit.default_timer() - ts_start)*1000))

if __name__ == '__main__':
	main()