def main():
	count = int(input())
	ceil_block = list(map(int, input().split()))
	floor_block = list(map(int, input().split()))
	ceil_min = min(ceil_block)
	floor_max = max(floor_block)
	if ceil_min > floor_max:
		print('Yes {}'.format(ceil_min - floor_max))
	else:
		print('No {}'.format(floor_max - ceil_min + 1))

if __name__ == '__main__':
	main()